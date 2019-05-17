class Node:
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_value = None

class linkedlist:
    def __init__(self):
        self.start_value = None

    def list_print(self):
        print_value = self.start_value
        while print_value != None:
            print(print_value.data_value)
            print_value = print_value.next_value

list = linkedlist()
list.start_value = Node(1)
next_2 = Node(2)
next_3 = Node(3)
list.start_value.next_value = next_2
next_2.next_value = next_3
list.list_print()
