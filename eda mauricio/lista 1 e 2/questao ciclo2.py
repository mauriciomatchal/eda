class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None

    def show_node(self):
        return str(self.value)


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
        if self.head is None:
            return False

        temp_1 = self.head
        temp_2 = self.head.prox

        while temp_2 is not None and temp_2.prox is not None:
            if temp_1 == temp_2:
                print('Cycle')
                return True
                break
            temp_1 = temp_1.prox
            temp_2 = temp_2.prox.prox

        return False

    def add(self):
        value, prox_value = input().split()

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = new_node

        if prox_value == 'None':
            new_node.prox = None
        else:
            temp = self.head
            while temp is not None:
                if temp.value == prox_value:
                    new_node.prox = temp
                    break
                temp = temp.prox

    def main(self):
        size = int(input("Enter the number of nodes: "))

        for _ in range(size):
            self.add()
            if self.check_cycle():
                break


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.main()
