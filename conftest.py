import pytest
import requests

from data import (
    BASE_URL,
    COURIER_LOGIN_ENDPOINT,
)
from courier import register_courier, delete_courier

# Создаёт уникального курьера перед тестом. После теста пытается авторизоваться под ним, получить id и удалить курьера.
@pytest.fixture
def courier():
    
    courier_data = register_courier()

    yield courier_data

    login_response = requests.post(
        f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
        data={
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    )

    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")

        if courier_id:
            delete_courier(courier_id)

# Создаёт курьера и возвращает его данные вместе с id. Используется там, где id нужен непосредственно в тесте.
@pytest.fixture
def registered_courier():
    
    courier_data = register_courier()

    login_response = requests.post(
        f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
        data={
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    )

    if login_response.status_code != 200:
        raise RuntimeError(
            f"Не удалось авторизовать тестового курьера: "
            f"{login_response.status_code} {login_response.text}"
        )

    courier_id = login_response.json()["id"]

    yield {
        "data": courier_data,
        "id": courier_id
    }

    delete_courier(courier_id)
