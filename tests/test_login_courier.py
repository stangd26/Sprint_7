import allure
import requests

from data import (
    BASE_URL,
    COURIER_LOGIN_ENDPOINT,
    LOGIN_REQUIRED_FIELDS_ERROR,
    LOGIN_INVALID_ERROR,
)


@allure.feature("Курьер")
@allure.story("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            data={
                "login": courier["login"],
                "password": courier["password"]
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Нельзя авторизоваться без login")
    def test_login_without_login(self, courier):
        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            data={
                "password": courier["password"]
            }
        )

        assert response.status_code == 400
        assert LOGIN_REQUIRED_FIELDS_ERROR in response.text

    @allure.title("Нельзя авторизоваться без password")
    def test_login_without_password(self, courier):
        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            data={
                "login": courier["login"]
            }
        )

        assert response.status_code == 504
        

    @allure.title("Ошибка при неправильном login")
    def test_login_with_wrong_login(self, courier):
        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            data={
                "login": "wrong_login",
                "password": courier["password"]
            }
        )

        assert response.status_code == 404
        assert LOGIN_INVALID_ERROR in response.text

    @allure.title("Ошибка при неправильном password")
    def test_login_with_wrong_password(self, courier):
        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            data={
                "login": courier["login"],
                "password": "wrong_password"
            }
        )

        assert response.status_code == 404
        assert LOGIN_INVALID_ERROR in response.text

    @allure.title("Ошибка при авторизации несуществующего пользователя")
    def test_login_nonexistent_courier(self):
        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            data={
                "login": "nonexistent_login",
                "password": "nonexistent_password"
            }
        )

        assert response.status_code == 404
        assert LOGIN_INVALID_ERROR in response.text
