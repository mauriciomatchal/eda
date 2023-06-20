class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.dir = None
        self.esq = None
    def show_node(self):
        return f'{self.value}'
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.prox = node
            self.tail = node
            
    def get_temp(self):
        temp = self.head
        return temp

class Tree:
    def __init__(self) -> None:
        self.root = None
    def add(self, node):
        node = Node(node)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            index = 0
            while queue[index] is not None:
                temp = queue[index]
                if temp.left is None:
                    temp.left = node
                    break
                elif temp.right is None:
                    temp.right = node
                    break
                queue.append(temp.left)
                queue.append(temp.right)
                index += 1
    def add(self, node):
        node = Node(node)
        if self.root is None:
            self.root = node
        else:
            q = Queue()
            q.add(self.root)
            temp = q
        while q.get_temp() is not None:
            temp = q.get_temp() # -> Node(1)
            temp = self.root
            while True:
                if temp.value == q.get_temp():
                    break
                else
            if temp.left is None:
                temp.left = node
                break
            elif temp.right is None:
                temp.right = node
            q.add(temp_value.left)
            q.add(temp_value.right)
            temp

    

def main():
    t = Tree()
    nodes = input().split()
    
if __name__ == '__main__':
    main()