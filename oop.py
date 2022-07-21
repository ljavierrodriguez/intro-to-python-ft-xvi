""" 
Abstracion, Encapsulamiento, Polimorfismo y Herencia
"""

class Person:
    name = None
    lastname = None
    age = None

    def __init__(self, name = "John", lastname = "Doe", age = "Unknow"):
        self.name = name
        self.lastname = lastname
        self.age = age

    def comer(self):
        return

    def correr(self):
        print("Person running")


class Student(Person):
    college = None

    def __init__(self, name = "John", lastname = "Doe", age = "Unknow", college = "MIT"):
        super().__init__(name, lastname, age)
        self.college = college

    def correr(self):
        print("Student running")


est1 = Student("Jane", "Doe", 29, "Harvard")
print(est1.name)
print(est1.college);

est1.correr()