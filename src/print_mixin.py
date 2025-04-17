class PrintMixin:
    """Миксин-класс, предоставляющий функциональность автоматического вывода
    строкового представления объекта при его создании"""


    def __init__(self):
        """Конструктор миксина. При создании объекта выводит его строковое представление
        в консоль с помощью метода __repr__"""
        print(repr(self))


    def __repr__(self):
        """Возвращает строковое представление объекта в формате:
        ClassName('name', 'description', price, quantity)"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"