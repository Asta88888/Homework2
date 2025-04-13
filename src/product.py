from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс, представляющий продукт с ценой, описанием и количеством на складе."""
    name: str
    description: str
    price: float
    quantity: int
    product_list = []


    def __init__(self, name, description, price, quantity):
        """Конструктор класса Product, для создания нового экземпляра"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        """Позволяет складывать стоимость всех товаров на складе."""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


    @classmethod
    def new_product(cls, new_product):
        """Добавление нового продукта"""
        for product in cls.product_list:
            if product.name == new_product["name"]:
                product.quantity += new_product["quantity"]
                product.price = max(product.price, new_product["price"])
                return product
        new_item = cls(new_product["name"], new_product["description"], new_product["price"], new_product["quantity"])
        cls.product_list.append(new_item)
        return new_item


    @property
    def price(self):
        """Геттер для цены"""
        return self.__price


    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой на отрицательные суммы и на уменьшение цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            print(f"Понизить цену с {self.__price} до {new_price} или оставить прежней? yes/no")
            user_answer = input().lower()
            if user_answer == "yes":
                self.__price = new_price
                print(f"Цена изменена. Старая цена: {self.__price}, новая цена: {new_price}")
            else:
                print("Цена не изменена")
        else:
            self.__price = new_price
            print(f"Цена {new_price}")



if __name__ == "__main__":
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
    product.price = 200000
    print(product.price)
    print(product + product2)

# new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
# print(new_product.__dict__)
