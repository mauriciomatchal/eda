
class Node:
    def __init__(self, value):
        self.value = value
    def show(self):
        return f'Valor: {self.value}'
    
class StaticList:
    def __init__(self, size):
        self.current_size = 0
        self.maximum_size = size
        self.list = [None] * size #creates an empty list
    def insert(self, node):
        if self.current_size < self.maximum_size: #checks if the list is not full
            #stores a node of the type node that has a "self.value" "x" within itself

            self.list[self.current_size] = Node(node) #stores the node value
            self.current_size += 1
        else:
            print('List is full')
    def show(self):
        for x in range(self.current_size):
            print(f'{x}: {self.list[x].show()}')


def main():
    lista = StaticList(3)
    lista.insert(1)
    lista.insert(2)
    lista.insert(3)
    lista.insert(4)
    lista.show()

if __name__ == '__main__':
    main()
