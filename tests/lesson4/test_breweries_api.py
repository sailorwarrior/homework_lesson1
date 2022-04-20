import requests
import pytest

BASE_URL = 'https://api.openbrewerydb.org/breweries'


@pytest.mark.parametrize('urls',
                         [f'{BASE_URL}', f'{BASE_URL}?by_city=san_diego',
                          f'{BASE_URL}?by_name=cooper', f'{BASE_URL}?by_type=micro',
                          f'{BASE_URL}/madtree-brewing-cincinnati', f'{BASE_URL}/search?query=dog',
                          f'{BASE_URL}/autocomplete?query=dog'])
def test_check_response(urls):
    response_to_check = requests.request('GET', urls)
    assert response_to_check.status_code == 200


@pytest.mark.parametrize('param_name, param_value',
                         [('by_city', 'san%20diego'), ('by_dist', '38.8977,77.0365'), ('by_name', 'modern%20times'),
                          ('by_state', 'new_york'), ('by_postal', '44107-4020'), ('by_type', 'closed')])
def test_check_parameters_search(param_name, param_value):
    response_to_check = requests.request('GET', BASE_URL, params={param_name: param_value})
    assert response_to_check.status_code == 200


@pytest.mark.parametrize('page_num',
                         [-1, 0, 1, 406, pytest.param(407, marks=pytest.mark.xfail(
                             reason='407 is last page on the test running moment (april, 16, 14:23)'))])
def test_check_page_opening(page_num):
    response_to_check = requests.request('GET', BASE_URL, params={'page': page_num})
    response_json = response_to_check.json()
    assert len(response_json) == 20


@pytest.mark.parametrize('per_page_numbers',
                         [pytest.param(-1, marks=pytest.mark.xfail(reason='returns default per page number')), 0, 1, 25,
                          50, pytest.param(51, marks=pytest.mark.xfail(reason='max per page number is 50'))])
def test_check_per_page_function(per_page_numbers):
    response_to_check = requests.request('GET', BASE_URL, params={'per_page': per_page_numbers})
    response_json = response_to_check.json()
    assert len(response_json) == per_page_numbers


@pytest.mark.parametrize('brewery_id', ['madtree-brewing-cincinnati',
                                        pytest.param('xfail', marks=pytest.mark.xfail(reason='invalid id'))])
def test_check_get_brewery(brewery_id):
    response = requests.request('GET', f'{BASE_URL}/{brewery_id}')
    json = response.json()
    assert json['id'] == brewery_id


@pytest.mark.parametrize('query_string', [
    pytest.param('dog', marks=pytest.mark.xfail(reason='bug in search, returns invalid values at the end')),
    pytest.param('fish', marks=pytest.mark.xfail(reason='bug in search, returns invalid values at the end'))])
def test_check_brewery_search(query_string):
    response = requests.request('GET', f'{BASE_URL}/search?query={query_string}')
    json = response.json()
    actual_result = []
    expected_result = [True for el in json]
    for el in json:
        results = []
        for key in el.keys():
            try:
                temp_result = query_string in str(el[key]).lower()
                results.append(temp_result)
            except:
                continue
        actual_result.append(max(results))
    assert expected_result == actual_result
