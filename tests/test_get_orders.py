import allure
import requests

from data import BASE_URL, ORDERS_ENDPOINT


@allure.feature("Заказы")
@allure.story("Получение списка заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_returns_list(self):
        response = requests.get(f"{BASE_URL}{ORDERS_ENDPOINT}")

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)     
