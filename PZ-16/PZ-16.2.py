#Вариант 16
"""
Создайте класс  "Фрукт", который содержит информацию о наименовании и весе 
фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса 
"Фрукт" и содержат информацию о цвете. 
"""

class Fruit:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Наименование должно быть не пустым")
        self._name = value.strip()
    
    @property
    def weight(self) -> float:
        return self._weight
    
    @weight.setter
    def weight(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self._weight = float(value)

    def info(self) -> str:
        return f"{self.name}, вес: {self.weight} г"
    
class Apple(Fruit):
    """
    Apple наследует Fruit
    """

    def __init__(self, color: str, weight: float) -> None:
        super().__init__("Яблоко", weight)
        self.color = color
    
    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Цвет должен быть не пустой строкой")
        self._color = value.strip()
    
    def info(self) -> str:
        return f"{super().info()}, цвет: {self.color}"
    
class Orange(Fruit):
    def __init__(self, color: str, weight: float) -> None:
        super().__init__("Апельсин", weight)
        self.color = color

    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Цвет должен быть не пустой строкой")
        self._color = value.strip()
    
    def info(self) -> str:
        return f"{super().info()}, цвет: {self.color}"


apple  = Apple(weight=182, color="Красный")
orange = Orange(weight=210, color="Оранжевый")

print(apple.info())
print(orange.info())