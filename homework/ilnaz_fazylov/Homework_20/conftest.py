import pytest
import requests


@pytest.fixture()
def new_object_id():
    body = {
        "name": "Test_1",
        "data": {'color': 'blue', 'size': 'large'},
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(scope='session')
def all_tests_info():
    print('\nStart testing')
    yield
    print('Testing completed')


@pytest.fixture()
def test_info():
    print('\nbefore test')
    yield
    print('\nafter test')
