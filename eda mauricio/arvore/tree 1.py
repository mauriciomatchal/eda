class Node:
    def __init__(self, value):
        self.value = value
        self.esq = None
        self.dir = None
    def show_node(self):
        return f'{self.value}'
class Tree:
    def __init__(self):
        self.root = None
    #def insert(self):
    #    temp = self.head
    def print_out(self):
        if self.root is not None:
            temp = self.root