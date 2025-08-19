class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Имя: {self.name}\n'
              f'Дата рождения: {self.birth_date}\n'
              f'Профессия: {self.occupation}\n'
              f'Высшее образование: {'Да' if self.higher_education else 'Нет'}\n')


person1 = Person("Айнура", "15.03.2002", "Программист", True)
person2 = Person("Адилет", "10.10.2005", "Дизайнер", False)
person3 = Person("Санжар", "09.06.2003", "Системный администратор", True)


person1.introduce()
person2.introduce()
person3.introduce()
