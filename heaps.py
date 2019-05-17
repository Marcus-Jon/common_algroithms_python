import heapq

class heap():
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insert(self, x):
        heapq.heappush(self.heap, x)

    def remove(self):
        self.decrease_key(i, float("-inf"))
        self.remove_min()

    def decrease_key(self, x, new_val):
        self.heap[x] = new_val
        while(x != 0 and self.heap[self.parent(x)] > self.heap[x]):
            self.heap[x], self.heap[self.parent(x)] =
            (self.heap[self.parent(x)], self.heap[x])

    def get_min(self):
        return self.heap[0]

    def remove_min(self):
        return heapq.heappop(self.heap)

h = heap()

h.insert(3)
h.insert(2)
h.insert(15)
h.insert(5)
h.insert(4)
h.insert(45)

print h.get_min()
