import pytest
from endpoints.create_object import CreateObject
from endpoints.create_object import InvalidDataError
from endpoints.update_object import UpdateObject
from endpoints.get_objects import GetObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def process_invalid_data():
    return InvalidDataError


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint, delete_object_endpoint):
    payload = {"name": "Test_1", "data": {'color': 'blue', 'size': 'large'}}
    create_object_endpoint.create_new_object(payload)
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_object(object_id)


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
