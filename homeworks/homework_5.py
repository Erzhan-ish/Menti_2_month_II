from homeworks.distance import Distance

if __name__ == "__main__":
    d1 = Distance(100, "m")
    d2 = Distance(2, "km")
    d3 = Distance(50, "cm")

    print("Инициализация:")
    print(d1)  # 100 m
    print(d2)  # 2 km
    print(d3)  # 50 cm

    print("\nСложение:")
    print(d1 + d2)  # 2100 m
    print(d2 + d3)  # 2.0005 km

    print("\nВычитание:")
    print(d2 - d1)  # 1900 m
    # print(d1 - d2)  # Ошибка: нельзя отрицательное расстояние

    print("\nСравнение:")
    print(d1 < d2)   # True
    print(d2 > d3)   # True
    print(d1 == Distance(100, "m"))  # True
    print(d1 == Distance(100, "km")) # False
