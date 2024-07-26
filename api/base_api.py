import requests
from ReadConfig import BASE_URL

class BaseAPI:
    def __init__(self, token=None):
        self.base_url = BASE_URL
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get(self, endpoint, params=None, headers=None):
        combined_headers = self.headers.copy()
        if headers:
            combined_headers.update(headers)
        response = requests.get(f"{self.base_url}{endpoint}", params=params, headers=combined_headers)
        response.raise_for_status()
        return response.status_code, response.json()

    def post(self, endpoint, data=None, headers=None):
        combined_headers = self.headers.copy()
        if headers:
            combined_headers.update(headers)
        response = requests.post(f"{self.base_url}{endpoint}", json=data, headers=combined_headers)
        response.raise_for_status()
        return response.status_code, response.json()

    def put(self, endpoint, data=None, headers=None):
        combined_headers = self.headers.copy()
        if headers:
            combined_headers.update(headers)
        response = requests.put(f"{self.base_url}{endpoint}", json=data, headers=combined_headers)
        response.raise_for_status()
        return response.status_code, response.json()