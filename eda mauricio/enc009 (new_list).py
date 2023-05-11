class Node:
    def __init__(self, value) :
        self.value = value
        self.prox = None
    def show(self):
        return f'{self.value}'
class LinkedList:
    def __init__(self):
        self.head = None
    def new_list(self):
        if self.head is not None:
            print('    ')