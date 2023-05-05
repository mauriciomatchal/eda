class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_first(self, node):
        if self.head is not None:
            node.prox = self.head
            self.head = node
        else:
            self.head = node
    def append_last(self, x):
        if self.head is not None: # checks if the list is not empty
            temp = self.head # creates a pointer to the first element called "temp"
            while True:
                if temp.prox is None: # if the list has only one element
                    temp.prox = x # the next element is "x"
                    break
                temp = temp.prox
                # if there is another element after 1 the temp now points to this number
        else:
            self.head = x
            # if the list is empty the first is x
    def free_list(self):
        if self.head is not None:
            temp = self.head
            while True:
                if temp.prox is not None:
                    temp.prox = None 
                    self.head = None

                    print('Free list now')
                    break    
                else:
                    temp = None
        else:
            return 'List is already empty'
    def size_of(self):
        temp = self.head
        size = 0
        if self.head is None:
            print('List is empty')
        else:
            while True:
                if temp.prox is not None:
                    size += 1
                    temp = temp.prox
                else:
                    size += 1
                    break
            print(size)



    def show(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox


def main():

    lista = LinkedList()

    lista.append_last(Node(2))
    lista.append_last(Node(3))
    lista.append_last(Node(5))
    lista.append_last(Node(6))
    lista.show()

    #lista.free_list()
    #lista.show()

    lista.size_of()

if __name__ == '__main__':
    main()
