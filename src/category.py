from src.product import Product
from src.base_category_order import BaseEntity


class Category(BaseEntity):
    """Класс, представляющий категорию товаров."""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0


    def __init__(self, name, description, products):
        """Конструктор класса Category, для создания экземпляров класса"""
        super().__init__(name, description)
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    def __str__(self):
        """Возвращает строковое представление категории с общим количеством товаров."""
        total_products_count = sum([p.quantity for p in self.__products])
        return f"{self.name}, количество продуктов: {total_products_count} шт."


    def add_product(self, product):
        """Функция добавляет новый продукт в список продуктов"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError


    @property
    def products(self):
        """Геттер для вывода списка продуктов в виде строки"""
        return "\n".join(
            f"{str(product)}" for product in self.__products
        )


    @property
    def products_list(self):
        """Возвращает список объектов продуктов в категории."""
        return self.__products


    def middle_price(self):
        """Вычисляет среднюю цену всех товаров. Возвращает 0, если товаров нет"""
        try:
            common_price = sum(product.price for product in self.__products)
            common_quantity = len(self.__products)
            return common_price / common_quantity
        except ZeroDivisionError:
            return 0

    def get_info(self):
        return f"Категория: {self.name} — {self.description}"


# product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
# product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#
# category1 = Category(
#     "Смартфоны",
#     "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#     [product1, product2, product3],
# )
# category2 = Category(
#     "Телевизоры",
#     "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#     [product4],
# )
# print(category1.products)
# print(category2.products)
#
# print(str(product1))
# print(str(product2))
# print(str(product3))
# print(str(category2))
#
# print(category2.products)