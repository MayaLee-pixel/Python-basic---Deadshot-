# 1
class Laptop:
    def __init__(self, name, price, battery_capacity):
        self.name = name
        self.price = price
        self.battery_capacity = Battery(battery_capacity)


class Battery:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity


# 2
class Guitar:
    def __init__(self, name, price, string):
        self.string = GuitarString(string)
        self.name = name
        self.price = price


class GuitarString:
    def __init__(self, string):
        self.string = string


# 3
class Calc:
    @staticmethod
    def add_num(a, b, c):
        return a + b + c


# 4
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        ingredients = ['forcemeat', 'tomatoes']
        return cls(ingredients)

    @classmethod
    def bolognaise(cls):
        ingredients = ['bacon', 'parmesan', 'eggs']
        return cls(ingredients)


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)

pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self.__visitors_count = 0

    @property
    def visitors_count(self):
        return self.__visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self.__visitors_count = Concert.max_visitors_num
        else:
            self.__visitors_count = value


Concert.max_visitors_num = 60
concert = Concert()
concert.visitors_count = 500
print(concert.visitors_count)
print(Concert.max_visitors_num)

# 6
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    adress: str
    email: str
    birthday: str
    age: int


# 7

from collections import namedtuple

AddressBookDataClass_tuple = namedtuple('AddressBookDataClass_tuple',
                                       ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


# 8
class AddressBook(AddressBookDataClass_tuple):
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        super().__init__()

addressbook_1 = AddressBook('7', 'YoungSir', '555555555', 'UK', 'young_sir@mail.com', '01.01.2000', 23)

print(str(addressbook_1))


# 9
class Person:
    name = "John"
    age = 36
    country = "USA"

setattr(Person, 'age', 20)
print(Person.age)


# 10
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(1, 'Test Student')
setattr(student, 'email', 'test_student@mail.com')
student_email = getattr(student, 'email')
print(student_email)


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        temperature_f = (self._temperature * 1.8) + 32
        return temperature_f

temperature_today = Celsius(18)

print(temperature_today.temperature)

