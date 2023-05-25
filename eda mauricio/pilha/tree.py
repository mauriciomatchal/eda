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
    def add(self, node):
        if self.root is None:
            a = 0