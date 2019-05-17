class Node:
        # Generation of a binary tree, with only the root node.
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        # Function to insert data to the tree.
        if self.data:
            if data < self.data:
        # Compares if new data is less than or greater than the previous node.
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def print_tree(self):
        # Function that prints all the elements in the tree in order.
        # Print left side of the tree.
        if self.left:
            self.left.print_tree()
        # Print root node.
        print(self.data),
        # Print right side of the tree.
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert_node(6)
root.insert_node(18)
root.insert_node(3)
root.insert_node(13)
root.print_tree()
