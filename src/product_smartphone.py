from src.product import Product


class Smartphone(Product):
    """Класс, представляющий смартфон как товар. Наследуется от Product."""
    efficiency: float
    model: str
    memory: int
    color: str


    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Конструктор класса Smartphone, наследует параметры класса Product и добавляет свои параметры"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        """Складывает два объекта Smartphone по общей стоимости (price * quantity)"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


