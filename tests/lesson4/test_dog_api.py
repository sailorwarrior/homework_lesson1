import pytest
import requests

BASE_URL = 'https://dog.ceo/api'


@pytest.mark.parametrize('urls', [f'{BASE_URL}/breeds/list/all', f'{BASE_URL}/breeds/image/random',
                                  f'{BASE_URL}/breed/hound/images', f'{BASE_URL}/breed/hound/list',
                                  f'{BASE_URL}/breed/hound/images/random'])
@pytest.mark.parametrize('methods', ['GET', 'HEAD'])
def test_check_response(methods, urls):
    response_to_check = requests.request(methods, urls)
    assert response_to_check.status_code == 200


@pytest.mark.parametrize('params, expected_values',
                         [('Content-Type', 'application/json'), ('Accept-Ranges', 'bytes'),
                          pytest.param('Content-Length', '936',
                                       marks=pytest.mark.xfail(reason='content-Length = 937'))])
def test_check_header_params(params, expected_values):
    response_to_check = requests.request('GET', f'{BASE_URL}/breeds/list/all')
    assert response_to_check.headers[params] == expected_values


@pytest.mark.parametrize('number, sub_breed', [(0, 'afghan'), (1, 'basset'), (2, 'blood')])
def test_check_answer(number, sub_breed):
    response_to_check = requests.request('GET', f'{BASE_URL}/breed/hound/list')
    response_json = response_to_check.json()
    assert response_json['message'][number] == sub_breed


@pytest.mark.parametrize('names', ['status', 'message'])
def test_check_answer_length(names):
    response_to_check = requests.request('GET', f'{BASE_URL}/breed/hound/list')
    response_json = response_to_check.json()
    assert len(response_json[names]) == 7


@pytest.mark.parametrize('numbers', [pytest.param(0, marks=pytest.mark.xfail(reason='min length is 1')), 1, 50,
                                     pytest.param(51, marks=pytest.mark.xfail(reason='max length is 50'))])
def test_check_response_status(numbers):
    response_to_check = requests.request('GET', f'{BASE_URL}/breeds/image/random/{numbers}')
    response_json = response_to_check.json()
    assert len(response_json['message']) == numbers
