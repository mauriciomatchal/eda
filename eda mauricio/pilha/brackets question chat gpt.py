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
    def is_empty(self):
        return self.head is None
    def push(self, value):
        new_node = Node(value)
        new_node.prox = self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self.head.value
            self.head = self.head.prox
            return value   
    def check_expression(self, expression):
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in expression:
            if char in opening_brackets:
                self.push(char)
            elif char in closing_brackets:
                if self.is_empty() or self.pop() != bracket_pairs[char]:
                    return False      
        return self.is_empty()

def main():
    lista = Stack()
    expression = input("Enter an expression: ")
    if lista.check_expression(expression):
        print("Valid expression")
    else:
        print("Invalid expression")

if __name__ == '__main__':
    main()
