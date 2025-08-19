from datetime import datetime as dt
from time import sleep


def checktime_before_after(func):
    def wrapper(*args, **kwargs):
        start = dt.now()
        print(f"# функция была вызвана в {start.hour:02}:{start.minute:02}:{start.second:02} {start.day:02}/{start.month:02}/{start.year}")
        result = func(*args, **kwargs)
        end = dt.now()
        print(f"# функция была закончена в {end.hour:02}:{end.minute:02}:{end.second:02} {end.day:02}/{end.month:02}/{end.year}")
        return result
    return wrapper


@checktime_before_after
def hello_world():
    print("hello world")
    sleep(1)


hello_world()
