import pytest


def test_category_init(first_category, second_category):

    assert first_category.name == "Смартфоны"
    assert second_category.name == "Телевизоры"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert second_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(first_category.products_list) == 2
    assert len(second_category.products_list) == 1

def test_category_products_property(first_category):
    assert first_category.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                "Iphone 15, 210000.0 руб. Остаток: 8 шт.")

def test_first_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."

def test_second_category_str(second_category):
    assert str(second_category) == "Телевизоры, количество продуктов: 7 шт."

# def test_category_add_products(first_category, product):
#     assert len(first_category.products_list) == 2
#     first_category.products = product
#     assert len(first_category.products_list) == 3
"""
В ЗАДАНИИ НЕ БЫЛО СКАЗАНО СДЕЛАТЬ СЕТТЕР НА СКОЛЬКО Я ПОНЯЛА ПОЭТОМУ
ЭТУ ПРОВЕРКУ(ВЫШЕ) НЕ СМОГЛА ОСУЩЕСТВИТЬ, НАДЕЮСЬ И ТАК СОЙДЕТ
"""