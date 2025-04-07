import requests
import allure
from endpoints.endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):

    @allure.step('Update an object')
    def change_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Update the name of object')
    def change_object_name(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
