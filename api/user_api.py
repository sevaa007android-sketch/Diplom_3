import allure
import requests
from data import API_BASE_URL

@allure.step("Отправить запрос {method} {endpoint}")
def send_request(method, endpoint, **kwargs):
    url = f"{API_BASE_URL}{endpoint}"
    response = requests.request(method, url, **kwargs)
    return response

@allure.step("Регистрация пользователя")
def register_user(user_data):
    return send_request("POST", "/auth/register", json=user_data)

@allure.step("Удаление пользователя")
def delete_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    return send_request("DELETE", "/auth/user", headers=headers)