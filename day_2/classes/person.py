class Person:

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def name(self):
        return self.__name

    def talk(self):
        return f"Hi, my name is {self.__name} and I am {self.age} years old"

    def set_name(self, new_name):
        self.__name = new_name
