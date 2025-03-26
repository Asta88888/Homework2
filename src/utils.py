import json
import os
from typing import Any
from src.category import Category
from src.product import Product


def reader_json(path: str) -> dict[Any, Any]:
    """Функция для чтения JSON-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list) -> list[Category]:
    """Функция создает список объектов класса Product из JSON-данных"""
    categories = []
    for object in data:
        products = []
        for product in object["products"]:
            products.append(Product(**product))
        object["products"] = products
        categories.append(Category(**object))
    return categories


if __name__ == "__main__":
    data = reader_json("../data/products.json")
    objects_data = create_objects_from_json(data)
    print(objects_data[0].name)
    print(objects_data[1].name)
    print(objects_data[0].description)
    print(objects_data[1].description)
    print(objects_data[0].products)
    print(objects_data[1].products)
