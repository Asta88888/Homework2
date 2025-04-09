import pytest


def test_product_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_product_smartphone_init2(smartphone2):
    assert smartphone2.name == "Xiaomi Redmi Note 11"
    assert smartphone2.description == "1024GB, Синий"
    assert smartphone2.price == 31000.0
    assert smartphone2.quantity == 14
    assert smartphone2.efficiency == 90.3
    assert smartphone2.model == "Note 11"
    assert smartphone2.memory == 1024
    assert smartphone2.color == "Синий"


def test_product_smartphone_common_price(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 1334000.0


def test_product_smartphone_common_price_invalid(smartphone1, smartphone2):
    with pytest.raises(TypeError):
        result = smartphone1 + 1


