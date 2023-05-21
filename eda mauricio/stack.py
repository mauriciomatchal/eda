class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
    
class Stack:
    def __init__(self):
        self.head = None
    def insert_on_stack(self, node):
        if node.value == '(' or node.value == '{' or node.value ==  '[':
            node.prox = self.head
            self.head = node
        elif node.value == ')' or node.value == '}' or node.value == ']':
            temp = self.head
            if temp.prox is None:
                if node.value == ')' and temp.value == '(':
                    self.head = None
                elif node.value == '}' and temp.value == '{':
                    self.head = None
                elif node.value == ']' and temp.value == '[':
                    self.head = None
            else:
                temp = self.head
                temp2 = self.head
                while temp2.prox.prox is not None:
                    temp2 = temp2.prox
                while temp.prox is not None:
                    temp = temp.prox
                if node.value == ')' and temp.value == '(':
                    temp2 = None
                elif node.value == '}' and temp.value == '{':
                    temp2 = None
                elif node.value == ']' and temp.value == '[':
                    temp2 = None
        else:
            print('Invalid value')
    def check(self):
        temp = self.head
        if temp is None:
            print('Válido')
        else:
            print('Inválido')
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
    lista.insert_on_stack(Node('('))
    lista.insert_on_stack(Node(')'))
    lista.insert_on_stack(Node('{'))
    lista.insert_on_stack(Node('}'))
    lista.show()
    lista.check()
if __name__ == '__main__':
    main()



#def remove_from_stack(self):
    #    temp = self.head
    #    if self.head is None:
    #        print('No elements in list')
    #    else:
    #        self.head = temp.prox
    #        temp.prox = None

