from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")  # превращаем строку в дату рождения
        today = datetime.now()
        # вычисляем возраст (год сейчас - год рождения, корректируем если день рождения ещё не был в этом году)
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

    def get_occupation(self):
        return self.__occupation

    def has_higher_education(self):
        return self.__higher_education

    def introduce(self):
        education = "есть высшее образование" if self.__higher_education else "нет высшего образования"
        print(f"Меня зовут {self.name}. Я родился(ась) {self.__birth_date}. "
              f"Я работаю {self.__occupation.lower()}ом, у меня {education}.")


class Friend(Person):   # создаём класс Friend (друг), наследуется от Person
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        # конструктор наследует поля от Person и добавляет своё
        super().__init__(name, birth_date, occupation, higher_education)  # инициализация Person
        self.hobby = hobby   # новое поле — хобби

    def introduce(self):   # переопределяем метод "представиться"
        education = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}, я друг Игоря, "
              f"работаю {self.get_occupation().lower()}ом, мое хобби — {self.hobby}, у меня {education}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}, я одноклассник Игоря, учились вместе в {self.group_name}, "
              f"работаю {self.get_occupation().lower()}ом, у меня {education}.")


people = [
    Friend(name="Алмаз", birth_date="05.12.2005", occupation="Программист", higher_education=True, hobby="играть в шахматы"),
    Friend(name="Алия", birth_date="22.07.2001", occupation="Дизайнер", higher_education=True, hobby="рисование"),
    Classmate(name="Бектур", birth_date="11.09.1999", occupation="Инженер", higher_education=True, group_name="11 Д"),
    Classmate(name="Эльдар", birth_date="01.03.2004", occupation="Маркетолог", higher_education=False, group_name="10 Б")
]

for person in people:
    person.introduce()
    print(person.age)
