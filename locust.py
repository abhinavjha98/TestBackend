import time
from locust import HttpUser, task, between
import requests
import json

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # @task
    # def index_page(self):
    #     self.client.get(url="/hello")

    # @task
    # def slow_page(self):
    #     self.client.get(url="/api/m/test/")

    @task
    def test_unauthorized_api(self):
        data = '{"url":"https://www.facebook.com/abc.exe"}'
        json.loads(data)
        return self.client.post('http://localhost/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})