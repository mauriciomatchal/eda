class Node:
    def __init__(self, value):
        self.value = value
        self.esq = None
        self.dir = None
    def show_node(self):
        return f'{self.value}'
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, child, parent):
        if self.root is not None:
            #temp = self.root
            if child.value <= parent.value:
                parent.esq = Node(child)
            else:
                parent.dir = Node(child)
        else:
            self.root = Node(child)

def main():
    tree = Tree()
    tree.insert(1, 0)
    tree.insert(2, 1)
    
    
if __name__ == '__main__':
    main()