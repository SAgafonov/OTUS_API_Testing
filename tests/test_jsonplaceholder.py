import cerberus
import json
import pytest
import requests


def test_create_resource(url_for_jsonplaceholder, body_for_jsonplaceholder):
    schema = {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"},
    }
    v = cerberus.Validator()
    response = requests.post(url_for_jsonplaceholder, data=json.dumps(body_for_jsonplaceholder))
    assert response.status_code == 201
    assert v.validate(response.json(), schema)


@pytest.mark.parametrize("key, value", [("title", "test_tytle"),
                                        ("body", "test_body")
                                        ])
def test_update_resource(url_for_jsonplaceholder, key, value, body_for_jsonplaceholder):
    body_for_jsonplaceholder[key] = value
    response = requests.put(url_for_jsonplaceholder + f'/{body_for_jsonplaceholder["userId"]}',
                            data=json.dumps(body_for_jsonplaceholder))
    assert response.status_code == 200


@pytest.mark.parametrize("id_value, reponse_code", [("1", 200),
                                                    ("9874", 404),
                                                    ("!%40%23%24%25%5E%26*('%60", 404)])
def test_get_resource(url_for_jsonplaceholder, id_value, reponse_code):
    response = requests.get(url_for_jsonplaceholder + f'/{id_value}')
    assert response.status_code == reponse_code
