class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:
    instances = []

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances += [self]
    def get_expertise(self):
        return self.expertise
    def get_price(self):
        return Consts.BASE_PRICE[self.expertise]
    def upgrade(self):
        self.level += 1
        self.calc_capacity()
    def hire(self, person):
        if int(len(self.employees)) == int(self.capacity):
            raise WorkPlaceIsFull(Exception)
        else:
            self.employees.append(person)
            person.work_place = self
    def calc(self):
        return -self.calc_costs()
    @staticmethod
    def calc_all():
        summation = 0
        for i in WorkPlace.instances:
            summation += i.calc()
        return  summation

