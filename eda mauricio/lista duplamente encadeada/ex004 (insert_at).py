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
    def insert_at(self, node, position):
        if self.head is not None:
            temp = self.head
            if position == 0:
                node.prox = self.head
                
                self.head.ant = node
                self.head = node
            else:
                for i in range(position + 1): #TAKE 1 OFF THE RANGE() AND THE i IN THE LOWER IF, IF YOU WANT THE VALUES TO BEGIN FROM "1"
                    if i == position - 1: # the temp pointer stops one node before the desired insertion position
                        if temp.prox is None: # if the node is the last one in the list
                            node.ant = temp
                            temp.prox = node
                        else: # if it's not the last one
                            node.ant = temp
                            node.prox = temp.prox
                            temp.prox.ant = node
                            temp.prox = node
                        break
                    temp = temp.prox
        else:
            self.head = node
    def show(self):
        if self.head is not None:
            temp = self.head
            print('<->-----<->')
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
def main():
    l = DoubleList()
    l.append_last(Node(1))
    l.append_last(Node(2))
    l.append_last(Node(3))
    l.append_last(Node(4))
    l.show()
    l.insert_at(Node('*'), 5)
    l.show()
    
if '__main__' == __name__:
    main()
