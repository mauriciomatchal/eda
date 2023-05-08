class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None

    def show_node(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_last(self, x):
        if self.head is not None:  # checks if the list is not empty
            temp = self.head  # creates a pointer to the first element called "temp"
            while True:
                if temp.prox is None:  # if the list has only one element
                    temp.prox = x  # the next element is "x"
                    break
                temp = temp.prox
                # if there is another element after 1 the temp now points to this number
        else:
            self.head = x
            # if the list is empty the first is x

    #def delete_node(self, node):
    #    if self.head is None:  # if the list is empty, there's nothing to delete
    #        return
    #    if self.head == node:  # special case for deleting the head node
    #        self.head = self.head.prox
    #        return
    #    temp = self.head
    #    while temp.prox is not None:
    #        if temp.prox == node:  # found the node to delete
    #            temp.prox = node.prox
    #            node.prox = None
    #            return
    #        temp = temp.prox

    def delete_node(self, node):
        if self.head is None:
            return  # list is empty       
        #we have to use ".value" here because "self.head" data
        #is not an integer and is being compared
        #to an integer so it doesn't work, if we use ".value", however,
        #we can compare both values ->
        if self.head.value == node:
            self.head = self.head.prox
            return

        prev_node = self.head
        curr_node = self.head.prox
        while curr_node is not None:
            if curr_node.value == node:
                prev_node.prox = curr_node.prox
                curr_node.prox = None
                return
            prev_node = curr_node
            curr_node = curr_node.prox

    def show(self):
        if self.head is not None:
            print('<---->')
            temp = self.head
            while temp is not None:
                
                print(f'{temp.show_node()}')
                temp = temp.prox


def main():

    lista = LinkedList()

    lista.append_last(Node(1))
    lista.append_last(Node(2))
    lista.append_last(Node(3))
    lista.append_last(Node(4))
    lista.show()

    lista.delete_node(4)
    lista.show()

if __name__ == '__main__':
    main()
