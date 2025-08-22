from blessed import Terminal

term = Terminal()

# Словарь фруктов и их цветов
fruits = {
    "Apple": term.red,
    "Orange": term.darkorange,
    "Banana": term.yellow,
    "Grape": term.purple,
    "Watermelon": term.green,
    "Strawberry": term.crimson,
    "Kiwi": term.lime
}

# Вывод каждого фрукта в своем цвете
for fruit, color in fruits.items():      # запускайте командой в терминале: python homeworks/homework_6.py
    print(color + fruit + term.normal)
