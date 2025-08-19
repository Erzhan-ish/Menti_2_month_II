class Distance:                                     # Объявляем класс для представления расстояния с единицей измерения.

    # коэффициенты для перевода в метры
    _units_to_meters = {                            # Атрибут КЛАССА (общий для всех объектов):
        "cm": 0.01,                                 # 1 сантиметр = 0.01 метра
        "m": 1,                                     # 1 метр = 1 метр (базовая единица)
        "km": 1000                                  # 1 километр = 1000 метров
    }

    def __init__(self, value: float, unit: str = "m"):   # Конструктор: принимает числовое значение и строку-единицу
        if unit not in self._units_to_meters:
            raise ValueError(f"Unsupported unit: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):                                   # Магический метод для красивой печати объекта (print, f-string и т.п.).
        return f"{self.value} {self.unit}"               # Возвращаем строку вида "12.5 km".

    # конвертация в метры
    def to_meters(self):                                 # Метод экземпляра: переводит текущее расстояние в метры.
        return self.value * self._units_to_meters[self.unit]   # Умножаем значение на коэффициент для его единицы.

    # статический метод для пересчёта в любую единицу
    @staticmethod
    def convert(value_in_meters, unit):                  # Статический метод: не нужен self; работает с числами и строкой-единицей.
        if unit not in Distance._units_to_meters:        # Проверяем, что целевая единица поддерживается.
            raise ValueError(f"Unsupported unit: {unit}")# Если нет — исключение.
        return value_in_meters / Distance._units_to_meters[unit] # Пересчитываем из метров в требуемую единицу (делим на коэффициент).

    def __add__(self, other):                            # Магический метод сложения: a + b.
        if not isinstance(other, Distance):              # Складывать корректно можно только два Distance.
            return NotImplemented                        # Сообщаем Python, что операция для такого типа не реализована.
        # приведение к метрам
        total_meters = self.to_meters() + other.to_meters()   # Переводим оба расстояния в метры и складываем.
        # возвращаем в единицах self
        return Distance(self.convert(total_meters, self.unit), self.unit)  # Результат создаём в той же единице, что и у self.

    def __sub__(self, other):                            # Магический метод вычитания: a - b.
        if not isinstance(other, Distance):              # Разрешаем вычитать только Distance.
            return NotImplemented
        total_meters = self.to_meters() - other.to_meters()   # Переводим в метры и вычитаем.

        # доп задание: не позволяем отрицательные расстояния
        if total_meters < 0:                             # Если результат меньше нуля (физически бессмысленно в этой модели),
            raise ValueError("Resulting distance cannot be negative")  # поднимаем исключение.

        return Distance(self.convert(total_meters, self.unit), self.unit)  # Возвращаем новый Distance в единицах self.

    # 🔹 методы сравнения (доп. задание 2)
    def __eq__(self, other):                             # == : равенство расстояний
        return self.to_meters() == other.to_meters()     # Сравниваем в метрах (универсально для разных единиц).

    def __lt__(self, other):                             # < : меньше
        return self.to_meters() < other.to_meters()      # Сравнение тоже через метры.

    def __le__(self, other):                             # <= : меньше или равно
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):                             # > : больше
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):                             # >= : больше или равно
        return self.to_meters() >= other.to_meters()

