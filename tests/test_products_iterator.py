import pytest


def test_products_iterator_first(products_iterator_first_category):
    iter(products_iterator_first_category)
    assert products_iterator_first_category.index == 0
    assert next(products_iterator_first_category).name == "Samsung Galaxy C23 Ultra"
    assert next(products_iterator_first_category).name == "Iphone 15"
    with pytest.raises(StopIteration):
        next(products_iterator_first_category)


def test_products_iterator_second(products_iterator_second_category):
    iter(products_iterator_second_category)
    assert products_iterator_second_category.index == 0
    assert next(products_iterator_second_category).name == "55\" QLED 4K"
    with pytest.raises(StopIteration):
        next(products_iterator_second_category)

