from work_place import WorkPlace
import work_place

class Company(WorkPlace):
    def __init__(self, name):
        super(Company, self).__init__(name)
        self.expertise = "company"

    def calc_capacity(self):
        self.capacity = int(self.level)
        return int(self.level)

    def calc_costs(self):
        costs = int(work_place.Consts.BASE_PLACE_COST * self.level)
        return costs
