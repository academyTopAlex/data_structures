"""

Создайте базовый класс Shape для рисования плоских
фигур.
Определите методы:
■ Show() — вывод на экран информации о фигуре;
■ Save() — сохранение фигуры в файл;
■ Load() — считывание фигуры из файла.

"""
from abc import ABC, abstractmethod
import json


class Shape(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self, path: str):
        pass


class Rectangle(Shape):
    count = 0

    def __init__(self, w: int = 0, h: int = 0, x: int = 0, y: int = 0):
        self.__w = w
        self.__h = h
        self.x = x
        self.y = y
        Rectangle.count += 1

    def show(self):
        pass

    def save(self):
        with open(f"{self.__class__.__name__}{type(self).count}.json", "w", encoding="utf-8") as f:
            json.dump({
                "w": self.__w,
                "h": self.__h,
                "x": self.x,
                "y": self.y
            }, f, indent=4)

    def load(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            d: dict = json.load(f)
        self.__w = d.get("w")
        self.__h = d.get("h")
        self.x = d.get("x")
        self.y = d.get("y")

    def __str__(self):
        return str(self.__dict__)


t = Rectangle()
t.save()
# t.load("Rectangle.json")
# print(t)
