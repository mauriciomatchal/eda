
class Node:

    def __init__(self, value):
        self.value = value
    
    def show(self):
        return(f'Valor: {self.value}')

class StaticList:
    def __init__(self, size):
        self.current_size = 0
        self.maximum_size = size
        self.list = [None] * size #creates an empty list


    def insert(self, x):
        if self.current_size < self.maximum_size: #checks if the list is not full
            #stores a node of the type node that has a "self.value" "x" within itself

            self.list[self.current_size] = Node(x) #stores the
            self.current_size += 1
        else:
            print('List is full')

    def show(self):
        for x in range(self.current_size):
            print(f'{x}: {self.list[x].show()}')


def main():
    l = StaticList(3)
    
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    
    l.show()

if __name__ == '__main__':
    main()
