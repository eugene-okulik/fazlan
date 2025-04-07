import allure


class BaseEndpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that object id is the same as sent')
    def check_object_id_is_correct(self, object_id):
        assert self.json['id'] == object_id, 'id of object is incorrect'

    @allure.step('Check that object length is correct')
    def check_object_length_is_correct(self, length):
        assert len(self.json) == length, 'Length of object is incorrect'

    @allure.step('Check that name is the same as sent')
    def check_object_name_is_correct(self, name):
        assert self.json['name'] == name, 'Name of object is incorrect'

    @allure.step('Check that response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, 'Status code is incorrect'
