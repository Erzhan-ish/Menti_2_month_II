class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Меня зовут {self.name}. Я родился(ась) {self.birth_date}. Я работаю {self.occupation}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Игоря, я родился {self.birth_date}, "
              f"работаю {self.occupation.lower()}ом, мое хобби — {self.hobby}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Игоря, учились вместе в {self.group_name}, "
              f"я родился {self.birth_date}, работаю {self.occupation.lower()}ом")


people = [
    Friend(name="Алмаз", birth_date="05.12.2003", occupation="Программист", higher_education=True, hobby="играть в шахматы"),
    Friend(name="Алия", birth_date="22.07.2001", occupation="Дизайнер", higher_education=True, hobby="рисование"),
    Classmate(name="Бектур", birth_date="11.09.2005", occupation="Инженер", higher_education=True, group_name="11 Д"),
    Classmate(name="Эльдар", birth_date="01.03.2002", occupation="Маркетолог", higher_education=False, group_name="10 Б")
]


for person in people:
    person.introduce()

