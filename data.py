BASE_URL = "https://qa-scooter.praktikum-services.ru"

COURIER_CREATE_ENDPOINT = "/api/v1/courier"
COURIER_LOGIN_ENDPOINT = "/api/v1/courier/login"
ORDERS_ENDPOINT = "/api/v1/orders"
ORDER_CANCEL_ENDPOINT = "/api/v1/orders/cancel"

# Данные для заказа
ORDER_DATA = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, ул. Тверская, д. 1",
    "metroStation": 4,
    "phone": "+7 999 123-45-67",
    "rentTime": 3,
    "deliveryDate": "2026-12-31",
    "comment": "Тестовый заказ"
}

BLACK = ["BLACK"]
GREY = ["GREY"]
BOTH_COLORS = ["BLACK", "GREY"]

# Сообщения API, которые относятся к проверяемым негативным сценариям.
COURIER_DUPLICATE_ERROR = "Этот логин уже используется"
COURIER_REQUIRED_FIELDS_ERROR = "Недостаточно данных для создания учетной записи"
LOGIN_REQUIRED_FIELDS_ERROR = "Недостаточно данных для входа"
LOGIN_INVALID_ERROR = "Учетная запись не найдена"
SERVICE_UNAVAILABLE = "Service unavailable"