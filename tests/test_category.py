import pytest


def test_category_init(first_category, second_category):

    assert first_category.name == "Смартфоны"
    assert second_category.name == "Телевизоры"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert second_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(first_category.products) == 2
    assert len(second_category.products) == 1

