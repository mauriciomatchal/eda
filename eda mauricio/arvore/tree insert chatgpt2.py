class StackNode:
    def __init__(self, value):
        self.value = value
        self.prox = None

class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, node):
        node = StackNode(node)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = node
    def pop(self):
        if self.head is None:
            return None
        elif self.head.prox is None:
            saved_value = self.head.value
            self.head = None
            return saved_value
        else:
            temp = self.head
            while temp.prox.prox is not None:
                temp = temp.prox
            saved_value = temp.prox.value
            temp.prox = None
            return saved_value
class Node:
    def __init__(self, value):
        self.value = value
        self.esq = None
        self.dir = None
class Tree:
    def __init__(self):
        self.root = None
        self.s = Stack()
        
    def add(self, node):
        node = Node(node)
        if self.root is None:
            self.root = node
        else:
            temp = self.root
            while True:
                if node.value < temp.value:
                    if temp.esq is None:
                        temp.esq = node
                        break
                    else:
                        temp = temp.esq
                else:
                    if temp.dir is None:
                        temp.dir = node
                        break
                    else:
                        temp = temp.dir
    
    def read_input(self, input):
        for x in input:
            self.root = self.remove(self.root, x)
    def remove(self, temp, node):
        if temp is None:
            return temp
        if node > temp.value:
            temp.dir = self.remove(temp.dir, node)
        elif node < temp.value:
            temp.esq = self.remove(temp.esq, node)
        else:
            if temp.esq is None:
                return temp.dir
            elif temp.dir is None:
                return temp.esq
            else:
                lowest_node = self.lowest_node(temp.dir)
                temp.value = lowest_node
                temp.dir = self.remove(temp.dir, lowest_node)
        return temp

    def lowest_node(self, node):
        temp = node
        while temp.esq is not None:
            temp = temp.esq
        return temp.value
   
    def in_order(self, node, limit):
        if node is not None:
            if node.value != limit:
                self.in_order(node.esq, limit)
                print(node.value)
                self.in_order(node.dir, limit)
            else:
                return 
        else:
            return
            
    def in_order_limit(self, limit):
        stack = Stack()
        temp = self.root

        while True:
            if temp is not None:
                if temp is not None and temp.value == limit:
                    
                    break
                stack.push(temp)
                temp = temp.esq
            elif stack.is_empty():
                break
            else:
                a = f'{limit}'
                b = ''
                temp = stack.pop()
                while True:
                    if temp == limit:
                        return False
                    b += f'{temp.value}' + ' '
                b += a
                print(b)
                temp = temp.dir
                
def main():
    times = input()

    t = Tree()
    nodes = input().split()
    to_be_removed = [int(x) for x in input().split()]
    limit = int(input())
    for x in nodes:
        t.add(int(x))

    t.in_order(t.root, limit)
    #t.in_order_limit(limit)    
    
    #t.read_input(to_be_removed)
    print()
    #t.in_order_limit(limit)

if __name__ == '__main__':
    main()