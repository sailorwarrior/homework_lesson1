import requests


def test_check_response_answer(base_url, status_code):
    response = requests.request('GET', base_url)
    assert response.status_code == int(status_code)
