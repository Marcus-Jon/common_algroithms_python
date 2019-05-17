import array as ar

class array_class():
    def __init__(self):
        self.array_of_int = ar.array('i',[])
    def append(self, x):
        self.array_of_int.append(x)
    def change(self, y, x):
        self.array_of_int[y] = x
    def delete(self, x):
        del self.array_of_int[x]
    def insert(self, x, y):
        return self.array_of_int.insert(y, x)
    def remove(self, x):
        return self.array_of_int.remove(x)
    def print_array(self):
        print(self.array_of_int)

a = array_class()
a.append(2)
a.append(5)
a.append(54)
a.print_array()
a.remove(5)
a.print_array()
