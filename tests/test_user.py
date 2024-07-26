import pytest
from api.user_api import UserAPI
from api.auth_api import AuthAPI
from ReadConfig import EMAIL, PASSWORD

@pytest.fixture()
def user_api():
    auth_api = AuthAPI()
    token = auth_api.login(EMAIL, PASSWORD)
    if not token:
        pytest.fail("Failed to obtain token. Invalid credentials or another error.")
    return UserAPI(token)

def test_user_list(user_api):
    status_code, response = user_api.user_list()
    print(response)
    assert status_code == 200

# def test_get_user(user_api):
#     user_id = 2
#     status_code, response = user_api.get_user(user_id)
#     print(response)
#     assert status_code == 200

# def test_update_user(user_api):
#     user_id = 2
#     user_data = {"name": "Admin1"}
#     status_code, response = user_api.update_user(user_id, user_data)
#     print(response)
#     assert status_code == 200