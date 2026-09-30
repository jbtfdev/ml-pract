import tracemalloc

def read_all(path):
    with open(path) as f:
        return f.readlines()

def stream_lines(path):
    with open(path) as f:
        for line in f:
            yield line

tracemalloc.start()
result = read_all("data/big.csv")
print("read_all: ",tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
for line in stream_lines("data/big.csv"):
    pass
print("stream_lines: ", tracemalloc.get_traced_memory())
tracemalloc.stop()