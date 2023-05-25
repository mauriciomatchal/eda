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
    def empty(self):
        self.head = None
    def push(self, node):
        node = Node(node)
        node.prox = self.head
        self.head = node
    def pop(self):
        if self.head is None:
            print('Lista vazia')
        else:
            self.head = self.head.prox
    def check_valitude(self, vector):
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
        for i in vector:
            if i in opening_brackets:
                self.push(i)
            elif i in closing_brackets:
                if self.head is not None and bracket_pairs[i] == self.head.value:
                    self.pop()
                else:
                    return False        
        return self.head is None

def main():
    lista = Stack()
    if lista.check_valitude(input()):
        print("Valid expression")
    else:
        print("Invalid expression")
if __name__ == '__main__':
    main()
