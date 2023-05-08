class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
class Queue: # In a queue we insert nodes in the end and remove nodes from the beginning.
    def __init__(self):
        self.head = None
    def insert_queue(self,x ):
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
    def remove_queue(self):
        temp = self.head
        if self.head is None:
            print('No elements in list')
        else:
            self.head = temp.prox
            temp.prox = None
    def show(self):
        if self.head is not None:
            print('>--------<')
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
def main():
    lista = Queue()

    lista.insert_queue(Node(1))
    lista.insert_queue(Node(2))
    lista.insert_queue(Node(3))
    lista.insert_queue(Node(4))
    lista.show()
    
    lista.remove_queue()
    lista.show()

if __name__ == '__main__':
    main()
