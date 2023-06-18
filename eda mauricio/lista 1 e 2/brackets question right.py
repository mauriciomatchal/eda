class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
class Stack:
    def __init__(self):
        self.head = None
    def show(self):
        if self.head is not None:
            print('*** Pilha ***')
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
    # acts as a normal push method for stacks.
    def push(self, node):
        node = Node(node)
        node.prox = self.head
        self.head = node
    # acts as a normal pop method for stacks.
    def pop(self):
        if self.head is None:
            print('Lista vazia')
        else:
            self.head = self.head.prox
            
    def check_valitude(self, input):
        for x in input:
            if x == '(' or x == '[' or x == '{':
                self.push(x)
            elif x == ')' or x == ']' or x == '}':
                if self.head is None:
                    return False
                else:
                    if x == ')' and self.head.value == '(':
                        self.pop()
                    elif x == '}' and self.head.value == '{':
                        self.pop()
                    elif x == ']' and self.head.value == '[':
                        self.pop()
                    else:
                        return False
                    
        return self.head is None
    # checks if the outcome of the previous method is true or false
    # and assigns the corresponding outcome to each case.
    def input_(self):
        if self.check_valitude(input()) is True:
            print('Valido')
        else:
            print('Invalido')
def main():
    lista = Stack()
    lista.input_()
if __name__ == '__main__':
    main()
