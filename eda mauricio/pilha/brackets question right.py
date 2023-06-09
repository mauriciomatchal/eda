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
    # creates a dictionary with closing and opening brackets
    # then checks the input, if its an opening bracket i pushes
    # however if it's a closing one, it checks if the opening
    # corresponding bracket is atop of the stack, then it pops
    # if not it's invalid so it returns False.
    def check_valitude(self, input):
        opening = "([{"
        closing = ")]}"
        brackets = {')': '(', ']': '[', '}': '{'}
   
        for x in input:
            if x in opening:
                self.push(x)
            elif x in closing:
                if self.head is not None and brackets[x] == self.head.value:
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
