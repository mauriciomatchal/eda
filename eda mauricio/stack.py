class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
    
class Stack:
    def __init__(self):
        self.head = None
        self.temp = self.head
    def insert_on_stack(self, node):
        if self.head is None:
            self.head = node
        else:
            node.prox = self.head
            self.head = node
            temp_prox = self.temp.prox
            if self.temp.prox == ')':
                self.temp = None
                
            
            
    def show(self):
        if self.head is not None:
            print('*** Pilha ***')
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
                
def main():
    lista = Stack()

    lista.insert_on_stack(Node('('))
    lista.show()
    lista.insert_on_stack(Node('('))
    lista.show()
    lista.insert_on_stack(Node(')'))
    lista.show()

if __name__ == '__main__':
    main()



#def remove_from_stack(self):
    #    temp = self.head
    #    if self.head is None:
    #        print('No elements in list')
    #    else:
    #        self.head = temp.prox
    #        temp.prox = None

