import requests
import allure
from endpoints.endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    @allure.step('Get one object')
    def get_one_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.response

    @allure.step('Get all object')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response
