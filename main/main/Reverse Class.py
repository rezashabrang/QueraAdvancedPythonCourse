class Reverse:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if (len(self.data) == 0):
            raise StopIteration
        index = int(len(self.data) - 1)
        return self.data.pop(index)
