'''class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)

s = Stack()

print s.is_empty()
s.push("1")
s.push("2")
s.push("3")
print s.is_empty()
print s.size()
'''
# Queues------------------------------------------------------------------------
class Queue():
    def __init__(self):
        self.queue = list()
        self.max = 4
        self.head = 0
        self.tail= 0

    def add_queue(self, x):
        if self.size() >= self.max:
            return("FULL")
        self.queue.append(x)
        self.tail = self.tail + 1

    def remove_queue(self):
        if self.size() <= 0:
            self.reset()
            return("EMPTY")
        '''self.queue.pop(0)
        self.head = self.head + 1'''
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item

    def size(self):
        return self.tail - self.head

    def reset(self):
        self.queue = list()
        self.head = 0
        self.tail = 0

    def print_queue(self):
        print self.queue

q = Queue()
q.add_queue(1)
q.add_queue(2)
q.add_queue(3)
q.add_queue(4)
print(q.add_queue(5))
q.print_queue()

q.remove_queue()
q.remove_queue()
q.remove_queue()
q.print_queue()
