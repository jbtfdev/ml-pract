class Scaler:
    def __init__(self):
        self.mean = None 
        self.std = None 
    def fit(self,data):
        self.mean = sum(data) / len(data)
        variance =sum((x - self.mean) ** 2 for x in data) / len(data)
        self.std = (variance)**0.5

    def transform(self,data):
        s = (self.std or 1)
        return [(x - self.mean) / s for x in data]
    def __repr__(self):
        return f"Scaler(mean={self.mean}, std={self.std})"

# data = [10, 20, 30, 40, 50]
data  = [1, 2, 2, 3, 4]

sc = Scaler()

sc.fit(data)

result = sc.transform(data)

print(result)
print(sc)