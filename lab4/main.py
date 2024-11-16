from f4_1 import check_name, check_age
from fk4_2 import take_elbook
from f4_3 import update_profile
from f4_4 import find_user, book_order, discount_price
from f4_5 import register_user
from f4_7 import payment_book

# Функция вызова всех функций
def call_functions():
    #Вызов функций в заданной последовательности
    print("\nДействие 1:")
    try:
        check_name("a") # Ожидается ошибка без обработки
    except ValueError as pe:
        print(f"Введите возраст больше 18: {pe}")

    try:
        check_age(12) # Ожидается ошибка без обработки
    except PermissionError as ve:
        print(f"Введите имя правильно: {ve}")


    print("\nДействие 2:")
    take_elbook(0) # Обработка ошибки в процессе взятия книги

    print("\nДействие 3:")
    update_profile(1, -10) # Обработка с блоком finally

    print("\nДействие 4:")
    find_user(["Marat", "Murad", "Magomed"], 1) # Ошибка в поиске
    book_order(-10) # Ошибка в заказе
    discount_price(1000, 1000) # Ошибка в скидке

    print("\nДействие 5:")
    register_user("Marat", 18) # Ошибка при регистрации(пользователь уже существует)

    print("\nДействие 7:")
    payment_book(-1, -100) # Ошибка при оплате
# Примеры использования других пользовательских функций прописаны в шаге 4


if __name__ == "__main__":
    call_functions()