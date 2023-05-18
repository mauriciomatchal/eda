class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None

    def show_node(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_last(self, x):
        if self.head is not None:  # checks if the list is not empty
            temp = self.head  # creates a pointer to the first element called "temp"
            while True:
                if temp.prox is None:  # if the list has only one element
                    temp.prox = x  # the next element is "x"
                    break
                temp = temp.prox
                # if there is another element after 1 the temp now points to this number
        else:
            self.head = x
            # if the list is empty the first is x

    def insert_at(self, node, position):
        temp = self.head
        if position == 1:
            node.prox = self.head
            self.head = node    
        else:
            for i in range(position - 1):
                if i == position - 2:
                    node.prox = temp.prox
                    temp.prox = node
                else:
                    temp = temp.prox

    def show(self):
        if self.head is not None:
            print('<---->')
            temp = self.head
            while temp is not None:
                
                print(f'{temp.show_node()}')
                temp = temp.prox


def main():

    lista = LinkedList()

    lista.append_last(Node(1))
    lista.append_last(Node(2))
    lista.append_last(Node(3))
    lista.append_last(Node(4))
    lista.show()

    lista.insert_at(Node('*'), 5)
    lista.show()

if __name__ == '__main__':
    main()
