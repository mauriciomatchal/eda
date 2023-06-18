class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None

    def show_node(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        if self.head is not None:
            print('*** List ***')
            temp = self.head
            while temp is not None:
                print(temp.show_node())
                temp = temp.prox
        else:
            print('Empty list')

    def check_cycle(self):
        temp1 = self.head
        temp2 = self.head.prox
        
        if self.head is None:
            return False
        end = False

        while temp2 is not None and temp2.prox is not None:
            if temp1 == temp2:
                print('Ciclo')
                return True
                break
            temp1 = temp1.prox
            temp2 = temp2.prox.prox   
        return False
        
    def add(self):
        node, prox_node = input().split()
        node = Node(node)

        # insere o valor de node na lista
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = node

        # checa se o valor de prox_node existe na lista
        # se existe, ele cria o ciclo, se nao, ele ignora
        temp = self.head
        while temp is not None:
            if temp.value == prox_node:
                node.prox = temp
                break
            temp = temp.prox

def main():
    size = int(input())
    list = input().split()
    l = LinkedList()
    for _ in range(size - 1):
        l.add()
        if l.check_cycle():
            end = False
            break
        else:
            end = True
    
    if end is True:
        print('Sem Ciclo')
if __name__ == '__main__':
    main()
