import json
import re
from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)

PROJECTS = 'QTSOLBUG|QTSYSADM|QTJIRA|QSR|QDS|QTVSADDINBUG|QTWEBSITE|AUTOSUITE|PYSIDE|QTCOMPONENTS|QTIFW|QBS|QTMOBILITY|QTQAINFRA|QT3DS|QTCREATORBUG|QTBUG|QTWB|QTPLAYGROUND'
ISSUEPATTERN = re.compile(r'(('+PROJECTS+')-[0-9]{1,5})')

def get_proposed(data):
    proposed = []
    for requirement in data['requirements']:
        for comment in requirement['comments']:
            ids = re.findall(ISSUEPATTERN, comment['text'])
            if len(ids) > 0:
                for toid in ids:
                    fromid = requirement['id']
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
                    proposed.append(dep)
    return proposed

@app.route("/", methods=['POST'])
def main():
    data = request.get_json()
    if data is None or 'requirements' not in data:
    	abort(400, 'No requirements array in data posted!')
    proposed = get_proposed(data)
    return json.dumps(proposed)


if __name__ == '__main__':
    app.run()
