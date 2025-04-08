from locust import task, HttpUser
import random


class ObjectUser(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/object',
            json={
                "name": "Test_1",
                "data": {'color': 'blue', 'size': 'large'}
            },
            headers={'Content-Type': 'application/json'}
        )
        self.object_id = response.json()['id']

    @task(1)
    def get_one_object(self):
        self.client.get(
            f'/object/{self.object_id}'
        )

    @task(2)
    def get_all_object(self):
        self.client.get(
            '/object'
        )

    @task(3)
    def post_object(self):
        self.client.post(
            '/object',
            json={
                "name": random.choice([
                    'test_1_1',
                    'test_1_2',
                    'test_1_3'
                ]),
                "data": random.choice([
                    {'color': 'blue', 'size': 'large'},
                    {'color': 'red', 'size': 'small'},
                    {'color': 'green', 'size': 'medium'}
                ])
            },
            headers={'Content-Type': 'application/json'}
        )

    @task(1)
    def put_object(self):
        self.client.put(
            f'/object/{self.object_id}',
            json={
                "name": "Test_1_1",
                "data": {'color': 'blue', 'size': 'large'}
            },
            headers={'Content-Type': 'application/json'}
        )

    @task(1)
    def patch_object(self):
        self.client.patch(
            f'/object/{self.object_id}',
            json={
                "name": "Test_1_2"
            },
            headers={'Content-Type': 'application/json'}
        )

    def on_stop(self):
        self.client.delete(
            f'/object/{self.object_id}'
        )
