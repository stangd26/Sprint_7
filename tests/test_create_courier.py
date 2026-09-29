import allure
import requests

from data import (
    BASE_URL,
    COURIER_CREATE_ENDPOINT,
    COURIER_DUPLICATE_ERROR,
    COURIER_REQUIRED_FIELDS_ERROR,
)
from courier import generate_courier_data


@allure.feature("Курьер")
@allure.story("Создание курьера")
class TestCreateCourier:

    @allure.title("Можно создать нового курьера")
    def test_create_courier_success(self, created_courier):
        
        response = requests.post(
            f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
            data=created_courier
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_identical_couriers(self, created_courier):
        
        first_response = requests.post(
            f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
            data=created_courier
        )

        assert first_response.status_code == 201
        assert first_response.json() == {"ok": True}

        second_response = requests.post(
            f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
            data=created_courier
        )

        assert second_response.status_code == 409
        assert COURIER_DUPLICATE_ERROR in second_response.text


    @allure.title("Нельзя создать курьера без обязательного поля login")
    def test_create_courier_without_login(self):
        courier = generate_courier_data()
        courier.pop("login")

        response = requests.post(
            f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
            data=courier
        )

        assert response.status_code == 400
        assert COURIER_REQUIRED_FIELDS_ERROR in response.text

    @allure.title("Нельзя создать курьера без обязательного поля password")
    def test_create_courier_without_password(self):
        courier = generate_courier_data()
        courier.pop("password")

        response = requests.post(
            f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
            data=courier
        )

        assert response.status_code == 400
        assert COURIER_REQUIRED_FIELDS_ERROR in response.text

    @allure.title("Можно создать курьера без firstName")
    def test_create_courier_without_first_name(self, created_courier):
        courier = created_courier.copy()
        courier.pop("firstName")
        
        response = requests.post(
            f"{BASE_URL}{COURIER_CREATE_ENDPOINT}",
            data=courier
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}
