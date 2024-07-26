from .base_api import BaseAPI

class UserAPI(BaseAPI):
    def __init__(self, token):
        super().__init__(token)

    def user_list(self):
        return self.get("list")

    def get_user(self, user_id):
        return self.get(f"get/{user_id}")
    
    def update_user(self, user_id, user_data):
        return self.put(f"update/{user_id}", data=user_data)