import requests
from ReadConfig import BASE_URL

class AuthAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def login(self, email, password):
        try:
            response = requests.post(f"{self.base_url}login", json={"email": email, "password": password})
            response.raise_for_status()
            token = response.json().get("token")
            if not token:
                raise ValueError("Token not found in the response")
            return token
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            if response.status_code == 401:
                print(f"Error: {response.text[11:len(response.text)-2]}")
            else:
                print(f"Error: {response.text}")