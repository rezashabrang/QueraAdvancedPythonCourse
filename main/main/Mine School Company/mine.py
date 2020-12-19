from work_place import WorkPlace
import work_place
import math


class Mine(WorkPlace):
    def __init__(self, name):
        super(Mine, self).__init__(name)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = int(math.pow(int(self.level), 2))
        return int(math.pow(int(self.level), 2))

    def calc_costs(self):
        costs = int(int(work_place.Consts.BASE_PLACE_COST) + int(work_place.Consts.LEVEL_MUL)*int(self.level))
        return costs
