from src.base_category_order import BaseEntity
from src.product import Product
from src.category import Category


class Order(BaseEntity):
    """Класс заказа: содержит товар, количество и сумму заказа"""
    product: Product
    quantity: int


    def __init__(self, product: Product, quantity):
        """Конструктор класса Order, инициализирует новый заказ"""
        super().__init__(name=f"Заказ: {product.name}", description=product.description)
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total_price()


    def calculate_total_price(self):
        """Вычисляет итоговую стоимость заказа"""
        return self.product.price * self.quantity


    def get_info(self):
        """Возвращает подробную информацию о заказе"""
        return (f"{self.name}\n"
                f"Описание: {self.description}\n"
                f"Цена за штуку: {self.product.price}\n"
                f"Количество: {self.quantity}\n"
                f"Итог: {self.total_price} руб.")


    def __str__(self):
        """Возвращает краткое строковое представление заказа"""
        return f"{self.name} - {self.quantity}шт. на сумму {self.total_price}руб."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    order1 = Order(product1, 1)
    order2 = Order(product2, 2)
    print(order1)
    print(order2)
    smartphones = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [product1, product2])
    print(smartphones)
    print("Товары в категории:")
    print(smartphones.products)
    print("\nПодробно:")
    print(order1.get_info())
