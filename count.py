class CountUp:
    def __init__(self,limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter==self.limit:
            raise StopIteration
        else : self.counter = self.counter + 1
        return self.counter

for x in CountUp(5):
    print(x)