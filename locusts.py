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
    def test_unauthorized_api1(self):
        data = '{"url":"https://www.facebook.com/abc.exe"}'
        json.loads(data)
        return self.client.post(url='/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})
    
    @task
    def test_unauthorized_api2(self):
        data = '{"url":"https://www.intechhub.com/"}'
        json.loads(data)
        return self.client.post(url='/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})

    @task
    def test_unauthorized_api3(self):
        data = '{"url":"https://www.cimarexjobs.com/"}'
        json.loads(data)
        return self.client.post(url='/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})

    @task
    def test_unauthorized_api4(self):
        data = '{"url":"https://www.cpbint.com/"}'
        json.loads(data)
        return self.client.post(url='/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})

    @task
    def test_unauthorized_api5(self):
        data = '{"url":"https://www.chseb.com"}'
        json.loads(data)
        return self.client.post(url='/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})