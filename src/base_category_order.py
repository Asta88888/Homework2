from abc import ABC, abstractmethod


class BaseEntity(ABC):


    def __init__(self, name, description):
        self.name = name
        self.description = description


    @abstractmethod
    def get_info(self):
        pass