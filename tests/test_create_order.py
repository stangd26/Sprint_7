import allure
import pytest
import requests

from data import (
    BASE_URL,
    ORDERS_ENDPOINT,
    ORDER_DATA,
    BLACK,
    GREY,
    BOTH_COLORS,
)


@allure.feature("Заказы")
@allure.story("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize(
        "order_data",
        [
            pytest.param({**ORDER_DATA, "color": BLACK}, id="BLACK"),
            pytest.param({**ORDER_DATA, "color": GREY}, id="GREY"),
            pytest.param({**ORDER_DATA, "color": BOTH_COLORS}, id="BLACK_AND_GREY"),
            pytest.param(ORDER_DATA.copy(), id="WITHOUT_COLOR"),
        ]
    )
    @allure.title("Создание заказа с разными вариантами цвета")
    def test_create_order_with_different_colors(self, order_data, cleanup_orders):
        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json=order_data
        )

        assert response.status_code == 201

        track = response.json()["track"]
        cleanup_orders.append(track)

        assert "track" in response.json()
        assert isinstance(track, int)
        