from datetime import datetime as dt
from time import sleep


def checktime_before_after(func):     # определяем декоратор, принимающий функцию
    def wrapper(*args, **kwargs):
        start = dt.now()              # фиксируем время начала выполнения
        print(f"# функция была вызвана в {start.hour:02}:{start.minute:02}:{start.second:02} "
              f"{start.day:02}/{start.month:02}/{start.year}")

        result = func(*args, **kwargs)  # запускаем саму функцию и сохраняем результат

        end = dt.now()                 # фиксируем время окончания выполнения
        print(f"# функция была закончена в {end.hour:02}:{end.minute:02}:{end.second:02} "
              f"{end.day:02}/{end.month:02}/{end.year}")

        return result                  # возвращаем результат работы функции
    return wrapper


@checktime_before_after
def hello_world():
    print("hello world")
    sleep(1)


hello_world()

