from work_place import WorkPlace
import work_place
import math


class School(WorkPlace):
    def __init__(self, name):
        super(School, self).__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = int(math.floor(math.sqrt(self.level)))
        return int(math.floor(math.sqrt(self.level)))

    def calc_costs(self):
        costs = int(work_place.Consts.BASE_PLACE_COST* math.floor(math.sqrt(self.level)))
        return costs
