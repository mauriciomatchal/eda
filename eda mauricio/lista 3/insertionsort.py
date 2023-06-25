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
        self.max = MAX
        self.tam = 0
        self.list = [None] * MAX
    def add(self, node):
        """#"""
        if self.tam < self.max:
            node = Node(node)
            self.list[self.tam] = node
            self.tam += 1
        else:
            print('Full List')
    
    
    def show(self):
        """#"""
        string = ''
        for i in range(self.tam):
            string += f'{self.list[i].show_node()}' + ' '
        print(string)

def main():
    """#"""
    times = int(input())
    limit = int(input())
    lista_estatica = LE(times-1)
    for _ in range(times-1):
        lista_estatica.add(int(input()))
    lista_estatica.show()
if __name__ == '__main__':
    main()
