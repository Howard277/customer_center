from django.test import TestCase
import json
import time

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.birthday = time.time()


p = Person(name='wu', age=20)
print(type(p))
print(json.dumps(p.__dict__))
