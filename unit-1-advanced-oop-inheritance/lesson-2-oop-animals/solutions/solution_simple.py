class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError()


class Cat(Animal):
    def talk(self):
        return 'meow'


class Dog(Animal):
    def talk(self):
        return 'woof'
