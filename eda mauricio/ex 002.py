class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None
    def Insert(self, node):
        if self.head is not None:
            node.prox = self.head
            self.head = node
        else:
            self.head = node

    def Append(self, x):
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
    def show(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox


def main():

    lista = LinkedList()

    lista.Append(Node(2))
    lista.Append(Node(3))
    lista.Append(Node(5))

    lista.show()


if __name__ == '__main__':
    main()
