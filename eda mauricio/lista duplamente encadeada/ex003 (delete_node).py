class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None
        self.ant = None
    def show_node(self):
        return f'{self.value}'
class DoubleList:
    def __init__(self):
        self.head = None
    def append_last(self, node):
        if self.head is not None:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox #travels until it gets to the last node
            temp.prox = node
            node.ant = temp
        else:
            self.head = node
    
    def delete_node(self, node):
        if self.head.value == node:
            self.head = self.head.prox
            if self.head.value is not None:
                self.head.ant = None
        else:
            temp = self.head
            while temp is not None:
                if temp.value == node:
                    temp.ant.prox = temp.prox
                    if temp.prox is not None:
                        temp.prox.ant = temp.ant
                    temp.prox = None
                    temp.ant = None
                    break
                else:              
                    temp = temp.prox
    
    def show(self):
        if self.head is not None:
            print('<---->')
            temp = self.head
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
        
def main():
    l = DoubleList()
    l.append_last(Node(1))
    l.append_last(Node(2))
    l.append_last(Node(3))
    l.show()
    
    l.delete_node(1)
    l.show()
    
if '__main__' == __name__:
    main()