import requests
import allure
from endpoints.endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step('Delete one object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response
