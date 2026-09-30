class CountUp:
    def __init__(self,limit : int) -> None:
        self.limit = limit
        self.counter = 0

    def __iter__(self) -> "CountUp":
        return self

    def __next__(self) -> int:
        if self.counter==self.limit:
            raise StopIteration
        else : self.counter = self.counter + 1
        return self.counter

for x in CountUp(5):
    print(x)