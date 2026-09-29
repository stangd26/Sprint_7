import random
import string
import allure

import requests

from data import BASE_URL, COURIER_CREATE_ENDPOINT, COURIER_LOGIN_ENDPOINT

# Генерирует случайную строку из строчных латинских букв.
def generate_random_string(length=10):
    
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

# Создаёт уникальные данные нового курьера.
def generate_courier_data():
    
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

# Создаёт нового курьера. Возвращает: данные курьера, id курьера
@allure.step("Создание нового курьера")
def register_courier():
    
    courier = generate_courier_data()

    response = requests.post(
        f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
        data=courier
    )

    if response.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать тестового курьера: "
            f"{response.status_code} {response.text}"
        )

    return courier

# Удаляет курьера по id.
@allure.step("Удаление курьера по id")
def delete_courier(courier_id):
    
    response = requests.delete(
        f"{BASE_URL}{COURIER_CREATE_ENDPOINT}/{courier_id}"
    )

    return response

@allure.step("Удаление курьера по учетным данным")
def delete_courier_by_credentials(login, password):
    login_response = requests.post(
        f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
        data={
            "login": login,
            "password": password
        }
    )

    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            return delete_courier(courier_id)

    return None