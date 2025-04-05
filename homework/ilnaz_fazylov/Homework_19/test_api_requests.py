import requests
import pytest


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


def test_get_one_object(all_tests_info, test_info, new_object_id):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_object_id}').json()
    assert response['id'] == new_object_id


@pytest.mark.medium
def test_get_all_objects(test_info):
    response = requests.get('http://167.172.172.115:52353/object').json()
    assert len(response) == 1, 'Not all posts returned'


test_data = [
    ("test_1_1", {'color': 'blue', 'size': 'large'}),
    ("test_1_2", {'color': 'red', 'size': 'small'}),
    ("test_1_3", {'color': 'green', 'size': 'medium'}),
]


@pytest.mark.critical
@pytest.mark.parametrize("name, data", test_data)
def test_add_object(test_info, name, data):
    body = {
        "name": name,
        "data": data
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'


def test_put_object(test_info, new_object_id):
    body = {
        "name": "Test_1_1",
        "data": {'color': 'blue', 'size': 'large'},
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test_1_1'


def test_patch_object(test_info, new_object_id):
    body = {
        "name": "Test_1_2"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test_1_2'


def test_delete_object(test_info, new_object_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
