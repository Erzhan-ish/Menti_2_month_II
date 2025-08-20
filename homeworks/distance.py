class Distance:
    # словарь коэффициентов перевода единиц в метры
    _units_to_meters = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value: float, unit: str = "m"):
        if unit not in self._units_to_meters: # проверяем, поддерживается ли такая единица измерения
            raise ValueError(f"Не поддерживается:: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    # переводим текущее расстояние в метры
    def to_meters(self):
        return self.value * self._units_to_meters[self.unit]   # Умножаем значение на коэффициент для его единицы.

    # статический метод для пересчёта в любую единицу
    @staticmethod
    def convert(value_in_meters, unit):                  # Статический метод: не нужен self; работает с числами и строкой-единицей.
        if unit not in Distance._units_to_meters:
            raise ValueError(f"Не поддерживается: {unit}")
        return value_in_meters / Distance._units_to_meters[unit] # переводим метры в нужную единицу (например, метры → километры)

    def __add__(self, other): # Магический метод сложения: a + b.
        if not isinstance(other, Distance): # проверяем, что складываем с объектом Distance
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()   # Переводим оба расстояния в метры и складываем.
        return Distance(self.convert(total_meters, self.unit), self.unit)  # Результат создаём в той же единице, что и у self.

    def __sub__(self, other): # Магический метод вычитания: a - b.
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() - other.to_meters()   # Переводим в метры и вычитаем.
        if total_meters < 0: # доп задание: не позволяем отрицательные расстояния
            raise ValueError("Результат не может быть отрицательным")
        return Distance(self.convert(total_meters, self.unit), self.unit)

    # методы сравнения (доп. задание 2)
    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()

