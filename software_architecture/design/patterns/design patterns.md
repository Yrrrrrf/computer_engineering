# Design Patterns

Is a general, reusable solution to a commonly occurring problem within a given context in [[software]] design.
The design pattern is not a finished design that can be transformed directly into code. It is not a factor when using design patterns, that means that design patterns are [[programming language]] independent.


## Creational Patterns

### Singleton

Is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

```python

class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s = Singleton()

print(s)

s = Singleton.getInstance()

print(s)

s = Singleton.getInstance()

print(s)

```


### Factory Method

Is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

```python

class Dog:
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "Meow!"
    def __str__(self):
        return "Cat"

def get_pet(pet="dog"):

    """The factory method"""

    pets = dict(dog=Dog(), cat=Cat())

    return pets[pet]

d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())

```

### Abstract Factory

Is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

```python

class Dog:
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"

class Cat:

    def speak(self):
        return "Meow!"
    def __str__(self):
        return "Cat"

class PetFactory:

    """A simple factory"""

    def get_pet(self, pet="dog"):

        """The factory method"""

        pets = dict(dog=Dog(), cat=Cat())

        return pets[pet]

    def get_food(self, pet):

        """Concrete factory"""

        print("Factory has no idea what {} food is".format(pet))

class DogFactory(PetFactory):

    """Concrete factory"""

    def get_food(self):

        return "Dog food!"

class CatFactory(PetFactory):

    """Concrete factory"""

    def get_food(self):

        return "Cat food!"

def get_factory():

    """Factory producer"""

    return random.choice([DogFactory, CatFactory])()

# Create a concrete factory

factory = get_factory()

# Create a pet

pet = factory.get_pet()

# Pet speaks

print("Our pet is '{}'".format(pet))

print("Our pet says hello by '{}'".format(pet.speak()))

# What food does our pet eat?

print("Its food is '{}'".format(factory.get_food()))

```

### Builder

### Prototype

## Structural Patterns

### Adapter

### Bridge

### Composite

### Decorator

### Facade

### Flyweight

### Proxy

## Behavioral Patterns

### Chain of Responsibility

### Command

### Interpreter

### Iterator

### Mediator

### Memento

### Observer

### State

### Strategy

### Template Method

### Visitor

## Concurrency Patterns

### Active Object

### Balking

### Binding Properties

### Compute Kernel

### Double-Checked Locking

