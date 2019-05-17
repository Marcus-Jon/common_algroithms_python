from Queue import PriorityQueue

q = PriorityQueue()

q.put((1, "x"))
q.put((3, "y"))
q.put((2, "z"))


while not q.empty():
    next = q.get()
    print(next)
