import pytest
import allure
import requests


@allure.feature('Get')
@allure.story('Get one object')
@allure.title('Получение одного объектов')
def test_get_one_object(all_tests_info, test_info, new_object_id):
    with allure.step(f'Run get request for object with id {new_object_id}'):
        response = requests.get(f'http://167.172.172.115:52353/object/{new_object_id}').json()
    with allure.step(f'Check that object id is {new_object_id}'):
        assert response['id'] == new_object_id


@allure.feature('Get')
@allure.story('Get all objects')
@allure.title('Получение всех объектов')
@pytest.mark.medium
def test_get_all_objects(test_info):
    with allure.step('Run get request for all objects'):
        response = requests.get('http://167.172.172.115:52353/object').json()
    with allure.step('Check that object length is 1'):
        assert len(response) == 1, 'Not all posts returned'


test_data = [
    ("test_1_1", {'color': 'blue', 'size': 'large'}),
    ("test_1_2", {'color': 'red', 'size': 'small'}),
    ("test_1_3", {'color': 'green', 'size': 'medium'}),
]


@allure.feature('Create')
@allure.story('Create objects')
@allure.title('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize("name, data", test_data)
def test_add_object(test_info, name, data):
    with allure.step('Prepare test data'):
        body = {
            "name": name,
            "data": data
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to create an object'):
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.feature('Update')
@allure.story('Update all for an object')
@allure.title('Обновление имени и данных для объекта')
def test_put_object(test_info, new_object_id):
    with allure.step('Prepare test data for update'):
        body = {
            "name": "Test_1_1",
            "data": {'color': 'blue', 'size': 'large'},
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to update an object'):
        response = requests.put(
            f'http://167.172.172.115:52353/object/{new_object_id}',
            json=body,
            headers=headers
        ).json()
    with allure.step('Check object name is "Test_1_1"'):
        assert response['name'] == 'Test_1_1'


@allure.feature('Update')
@allure.story('Update name of object')
@allure.title('Обновление имени для объекта')
def test_patch_object(test_info, new_object_id):
    with allure.step('Prepare test data for update name'):
        body = {
            "name": "Test_1_2"
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to update the name of object'):
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{new_object_id}',
            json=body,
            headers=headers
        ).json()
    with allure.step('Check object name is "Test_1_2"'):
        assert response['name'] == 'Test_1_2'


@allure.feature('Delete')
@allure.story('Delete objects')
@allure.title('Удаление объекта')
@allure.issue(
    'https://cs14.pikabu.ru/post_img/2022/11/19/10/1668874431159454767.webp',
    'Bug-666'
)
@pytest.mark.high
def test_delete_object(test_info, new_object_id):
    with allure.step(f'Run delete request for object with id {new_object_id}'):
        response = requests.delete(f'http://167.172.172.115:52353/object/{new_object_id}')
    with allure.step('Check response code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'
