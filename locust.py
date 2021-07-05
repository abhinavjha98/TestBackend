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
<<<<<<< Updated upstream
        return self.client.post('http://20.98.205.93/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})
=======
        return self.client.post(url='/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})
>>>>>>> Stashed changes
