import math


class Person:
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.work_place = None
        self.job = ""
        Person.instances += [self]

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1
        return self.level

    def do_level(self, income):
        return income*math.sqrt(self.work_place.level*self.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        return self.do_level(self.calc_income()) - self.calc_life_cost()

    @staticmethod
    def calc_all():
        summation = 0
        for j in Person.instances:
            summation += j.calc()
        return summation




