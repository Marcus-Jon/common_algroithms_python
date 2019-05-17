class list():
    def __init__(self):
        self.list = []
    def insert(self, y, x):
        self.list.insert(y, x)
    def append(self, x):
        self.list.append(x)
    def remove(self, x):
        return self.list.remove(x)
    def pop(self, x):
        return self.list.pop(x)
    def index(self, x):
        print self.list.index(x)
    def print_list(self):
        print self.list
    def print_value(self, x):
        print self.list[x]

l = list()
l.append(4)
l.append("six")
l.append(25)
l.append("one")
l.print_list()
l.insert(4, 14)
l.print_list()
