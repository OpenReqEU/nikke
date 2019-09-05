import code as nikke
import os
import json
import pytest

def test_post_project():
    nikke.app.config['TESTING'] = True

    current_path = os.path.realpath(__file__)
    current_dir = os.path.dirname(current_path)
    complete_path = os.path.join(current_dir, "QTWB.json")
    data = json.loads(open(complete_path).read())

    response = nikke.app.test_client().post('/', json=data)
    deps = json.loads(response.data)
    assert(len(deps)>0)

def test_post_nothing():
    data = "[]"

    response = nikke.app.test_client().post('/', json=data)
    assert(response.status_code==400)
