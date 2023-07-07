"""#"""
class Node:
    """#"""
    def __init__(self, value):
        self.value = value
    def show_node(self):
        """#"""
        return f'{self.value}'

class LE:
    """#"""
    def __init__(self, MAX):
        self.MAX = MAX
        self.tam = 0
        self.list = [None] * MAX
    def show(self):
        """#"""
        string = ''
        for i in range(self.tam):
            string += f'{self.list[i].show_node()}' + ' '
        print(string)
    def add(self, node):
        """#"""
        if self.tam < self.MAX:
            node = Node(node)
            self.list[self.tam] = node
            self.tam += 1
        else:
            print('Full List')
            
    def insert_from_list(self, list):
        for i in list
    def insertion_sort(self, limit):
        position = self.tam
        used_limit = 0
        for i in range(self.tam - 1):
            if used_limit <= limit:
                if self.tam == 1:
                    used_limit += 1
                else:
                    if self.list[position-1].value < self.list[position-2].value:
                        self.list[position-1], self.list[position-2] = self.list[position-2], self.list[position-1]
                        position -= 1
                        used_limit += 1
                    else:
                        break
            else:
                break
                return
def main():
    """#"""
    times = int(input())
    limit = int(input())
    lista_estatica = LE(times-1)
    dump = LE(times-1)
    for i in range(times-1):
        lista_estatica.add(int(input()))
    for i in range(times-1):
        lista_estatica.insertion_sort(limit)
    lista_estatica.show()
if __name__ == '__main__':
    main()
