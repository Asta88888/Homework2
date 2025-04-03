from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_new_product():
    pr = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    pr.name = "Samsung Galaxy S23 Ultra"
    pr.description = "256GB, Серый цвет, 200MP камера"
    pr.price = 180000.0
    pr.quantity = 5

def test_product_str(product):
    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_add(product, product2):
    result = product + product2
    expected = 180000.0 * 5 + 123000.0 * 7
    assert result == expected