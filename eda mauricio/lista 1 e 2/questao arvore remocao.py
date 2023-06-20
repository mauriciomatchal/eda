class QueueNode:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_stack_node(self):
        return f'{self.value}'
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, node):
        node = QueueNode(node)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.prox = node
            self.tail = node
    def take_off(self):
        if self.head is None:
            print('Empty List')
        else:
            self.head = self.head.prox
    def limit(self, limit):
        temp = self.head
        str = ''
        while temp is not None:
            if temp.value == limit:
                str += f'{temp.show_stack_node()}'
                break
            else:
                str += f'{temp.show_stack_node()}' + ' '
            temp = temp.prox
        print(str)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.esq = None
        self.dir = None
class Tree:
    def __init__(self):
        self.root = None
        self.fila = Queue()
        self.filaremovidos = Queue()
    def add(self, node):
        node = TreeNode(node)
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
    
    def remove(self, node):
        self.root = self.remove_algorithm(self.root, node)
            
    def remove_algorithm(self, temp, value):
        if temp is None:
            return None
        elif value < temp.value:
            temp.esq = self.remove_algorithm(temp.esq, value)
        elif value > temp.value:
            temp.dir = self.remove_algorithm(temp.dir, value)
        else:
            if temp.esq is None and temp.dir is None:
                return None
            elif temp.esq is None:
                return temp.dir
            elif temp.dir is None:
                return temp.esq
            else:
                min_value = self.lowest_value(temp.dir)
                temp.value = min_value
                temp.dir = self.remove_algorithm(temp.dir, min_value)
        return temp

    def lowest_value(self, node):
        current = node
        while current.esq is not None:
            current = current.esq
        return current.value
    
    def in_order_limit(self, node):
        if node is not None:
            self.in_order_limit(node.esq)
            self.fila.insert(node.value)
            self.in_order_limit(node.dir)
            
    def in_order_limit2(self, node):
        if node is not None:
            self.in_order_limit2(node.esq)
            self.filaremovidos.insert(node.value)
            self.in_order_limit2(node.dir)
            
            
    def print_values(self, limit):
        self.fila.limit(limit)
    
    def print_values2(self, limit):
        self.filaremovidos.limit(limit)

    def show(self):
        if self.root is None:
            print('Empty List')
        else:
            self.in_order_limit(self.root)

def main():
    times = input()
    t = Tree()
    nodes = input().split()
    for x in nodes:
        t.add(int(x))
    remove1, remove2 = input().split()
    remove1 = int(remove1)
    remove2 = int(remove2)
    limit = int(input())
    
    t.in_order_limit(t.root)    
    t.print_values(limit)
    t.remove(remove1)
    t.remove(remove2)
    t.in_order_limit2(t.root)
    t.print_values2(limit)

if __name__ == '__main__':
    main()