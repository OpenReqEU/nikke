import json
import re
import os
from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)

app.config.from_pyfile("nikke.conf", silent=False)
PROJECTS = app.config.get("PROJECTS")
ISSUEPATTERN = re.compile(r'(('+PROJECTS+')-[0-9]{1,5})')

def get_proposed(data):
    proposed = []
    for requirement in data['requirements']:
        texts = []
        fromid = requirement['id']
        if 'text' in requirement:
            texts.append(requirement['text'])
        if 'comments' in requirement:
            for comment in requirement['comments']:
                texts.append(comment['text'])
        new_proposed = proposed_from_texts(fromid, texts)
        if new_proposed:
            proposed.extend(new_proposed)
    return proposed

def proposed_from_texts(fromid, texts):
    new_proposed = []
    for text in texts:
        ids = re.findall(ISSUEPATTERN, text)
        if len(ids) > 0:
            for toid in ids:
                dep = {
                    'id': '_'.join([fromid, toid[0], 'SIMILAR']),
                    'dependency_type': 'similar',
                    'dependency_score': 1.0,
                    'status': 'proposed',
                    'fromid': fromid,
                    'toid': toid[0],
                    'description': [
                        'Nikke'
                    ],
                    'created_at': 0
                }
                new_proposed.append(dep)
    return new_proposed

@app.route("/", methods=['POST'])
def main():
    data = request.get_json()
    if data is None or 'requirements' not in data:
    	abort(400, 'No requirements array in data posted!')
    proposed = get_proposed(data)
    return json.dumps(proposed)


if __name__ == '__main__':
    response.timeout = 1000
    app.run()
