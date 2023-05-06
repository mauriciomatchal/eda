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

    def show(self):
        if self.head is not None:
            print('<---->')
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox


def main():
    lista = LinkedList()

    lista.insert_first(Node(1))
    lista.insert_first(Node(2))
    lista.insert_first(Node(3))
    lista.insert_first(Node(4))
    lista.show()

if __name__ == '__main__':
    main()
