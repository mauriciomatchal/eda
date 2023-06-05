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
        
    def insert(self, place, node):
        if self.root is None:
            self.root = Node(node)
        else:
            if node.value >= place.value:
                if place.dir is not None:
                    self.insert(place.dir, node)
                else:
                    place.dir = node
            else:
                if place.esq is not None:
                    self.insert(place.esq, node)
                else:
                    place.esq = node
                    

def main():
    tree = Tree()
    tree.insert(1, 0)
    tree.insert(2, 1)
    
    
if __name__ == '__main__':
    main()