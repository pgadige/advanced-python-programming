# OOP Animals

Let's start with a simple assignment to practice your Inheritance skills.

The objective of this assignment is to create two subclasses of `Animal` named `Cat` and `Dog`. Every `Animal` will be created by passing a name, regardless of the type of Animal. For example:

```python
garfield = Cat(name='Garfield')
odie = Dog(name='Odie')

print(garfield.name)  # 'Garfield'
print(odie.name)      # 'Odie'
```

Every animal will have the ability to emit a sound, or as we'll friendly say it, every animal will be able to talk. That's why the `Animal` class has a `talk` method which is not implemented. All `Animal` subclasses will have to properly implement the `talk` method. This method is really simple and it just needs to return a string. A `Cat` `"meow"`s and a `Dog` `"woof"`s. Example:

```python
garfield.talk()  # 'meow'
odie.talk()      # 'woof'
```
