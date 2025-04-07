import pytest
import allure

TEST_DATA = [
    {'name': 'test_1_1', 'data': {'color': 'blue', 'size': 'large'}},
    {'name': 'test_1_2', 'data': {'color': 'red', 'size': 'small'}},
    {'name': 'test_1_3', 'data': {'color': 'green', 'size': 'medium'}}
]

NEGATIVE_DATA = [
    {'name': 1, 'data': {'color': 'red', 'size': 'small'}},
    {'name': 'test_1_3', 'data': False}
]


@allure.feature('Get')
@allure.story('Get one object')
@allure.title('Получение одного объектов')
def test_get_one_object(get_object_endpoint, all_tests_info, test_info, object_id):
    get_object_endpoint.get_one_object(object_id)
    get_object_endpoint.check_object_id_is_correct(object_id)


@allure.feature('Get')
@allure.story('Get all objects')
@allure.title('Получение всех объектов')
@pytest.mark.medium
def test_get_all_object(get_object_endpoint, test_info):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_object_length_is_correct(1)


@allure.feature('Create')
@allure.story('Create object')
@allure.title('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_object(test_info, create_object_endpoint, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_status_is_200()
    create_object_endpoint.check_object_name_is_correct(data['name'])


@allure.feature('Negative')
@allure.story('Create object with negative data')
@allure.title('Создание объекта с не валидными данными')
@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(test_info, create_object_endpoint, process_invalid_data, data):
    with pytest.raises(process_invalid_data):
        create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_bad_request()


@allure.feature('Update')
@allure.story('Update all for an object')
@allure.title('Обновление имени и данных для объекта')
def test_put_object(test_info, update_object_endpoint, object_id):
    payload = {
        "name": "Test_1_1",
        "data": {'color': 'blue', 'size': 'large'},
    }
    update_object_endpoint.change_object(object_id, payload)
    update_object_endpoint.check_object_name_is_correct(payload['name'])


@allure.feature('Update')
@allure.story('Update name of object')
@allure.title('Обновление имени для объекта')
def test_patch_object(test_info, update_object_endpoint, object_id):
    payload = {
        "name": "Test_1_2"
    }
    update_object_endpoint.change_object_name(object_id, payload)
    update_object_endpoint.check_object_name_is_correct(payload['name'])


@allure.feature('Delete')
@allure.story('Delete objects')
@allure.title('Удаление объекта')
@allure.issue(
    'https://cs14.pikabu.ru/post_img/2022/11/19/10/1668874431159454767.webp',
    'Bug-666'
)
@pytest.mark.high
def test_delete_object(test_info, delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_status_is_200()
