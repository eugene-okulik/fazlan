import requests
import allure
from endpoints.endpoint import BaseEndpoint


class InvalidDataError(Exception):
    pass


class CreateObject(BaseEndpoint):
    object_id = None

    @allure.step('Create new object')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        if self.response.status_code == 400:
            raise InvalidDataError('Invalid data format')
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
