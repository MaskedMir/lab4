# Классы пользовательских исключений, наследованных от базового Exception

class InvalidOrderError(Exception):
    print(" исключение для некорректного заказа")

class UserNotFoundError(Exception):
    print("исключение для отсутствующего пользователя")

class PaymentError(Exception):
    print("исключение для ошибок при оплате")