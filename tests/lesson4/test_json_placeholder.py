import requests
import pytest
from jsonschema import validate

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


@pytest.mark.parametrize('urls', [BASE_URL, f'{BASE_URL}/1'])
def test_check_response(urls):
    response = requests.request('GET', urls)
    assert response.status_code == 200


@pytest.mark.parametrize('ids', [pytest.param(-1, marks=pytest.mark.xfail(reason='Invalid negative value')),
                                 pytest.param(0, marks=pytest.mark.xfail(reason='Invalid zero value')), 1, 10,
                                 pytest.param(100000, marks=pytest.mark.xfail(reason='Value is too high'))])
def test_check_response_json_id(ids):
    response = requests.request('GET', f'{BASE_URL}/{ids}')
    response_json = response.json()
    assert response_json['id'] == ids


def test_validate_json_schema():
    response = requests.get(f'{BASE_URL}/1')
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string"}
        }
    }
    validate(instance=response.json(), schema=schema)


def test_check_resource_creation():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {
        'title': 'test_title',
        'body': 'test_body',
        'userId': 1, }
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             headers=headers, json=body)
    response_json = response.json()
    actual_result = {key: response_json[key] for key in body.keys()}
    assert actual_result == body


@pytest.mark.parametrize('parameters, values', [('userId', 1), ('id', 2)])
def test_filtering_results(parameters, values):
    response = requests.request('GET', BASE_URL, params={parameters: values})
    response_json = response.json()
    for el in range(len(response_json)):
        assert response_json[el][parameters] == values
