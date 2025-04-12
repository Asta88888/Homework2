from src.product import Product


class LawnGrass(Product):
    """Класс, представляющий газон как товар. Наследуется от Product."""
    country: str
    germination_period: str
    color: str


    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Конструктор класса LawnGrass, наследует параметры класса Product и добавляет свои параметры"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        """Складывает два объекта LawnGrass по общей стоимости (price * quantity)"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

