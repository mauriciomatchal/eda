
class Node:
    def __init__(self, value):
        self.value = value
    def show_node(self):
        return f'Valor: {self.value}'
        
class Static:
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
#
    def append_last(self, node):
        if self.current_size < self.maximum_size:
            self.list[self.maximum_size - 1] = Node(node)
        else:
            print('List is full')
#
    def show(self):
        for x in range(self.maximum_size):
            if self.list[x] is not None:
                print(f'{x}: {self.list[x].show_node()}')
            else:
                print(f'{x}: Valor: None')

def main():
    lista = Static(10)
    lista.insert(1)
    lista.insert(2)
    lista.insert(3)
    lista.append_last(9)
    lista.append_last(8)
    lista.show()

if __name__ == '__main__':
    main()
