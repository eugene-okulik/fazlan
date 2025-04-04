import requests


def all_objects():
    response = requests.get('http://167.172.172.115:52353/object').json()
    assert len(response) == 1, 'Not all posts returned'


def new_object():
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
    return response.json()['id']


def one_object():
    object_id = new_object()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}').json()
    assert response['id'] == object_id


def post_a_object():
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
    assert response.status_code == 200, 'Status code is incorrect'


def clear(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def put_a_post():
    object_id = new_object()
    body = {
        "name": "Test_1_1",
        "data": {'color': 'blue', 'size': 'large'},
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test_1_1'
    clear(object_id)


def patch_a_post():
    object_id = new_object()
    body = {
        "name": "Test_1_2"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test_1_2'
    clear(object_id)


def delete_a_post():
    object_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response.status_code)


post_a_object()
