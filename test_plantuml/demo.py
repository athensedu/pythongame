
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("walk()")


class Cat(Animal):
    def meow(self):
        print("meow()")


