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
        self.menores = LE(self.tam)
        self.maiores = LE(self.tam)
    def show(self):
        """#"""
        string = ''
        for i in range(self.tam):
            string += f'{self.list[i].show_node()}' + ' '
        print(string)
    def add(self, node):
        """#"""
        if self.tam < self.max:
            node = Node(node)
            self.list[self.tam] = node
            self.tam += 1
        else:
            print('Full List')
    def quick_sort(self, limit):
        pivot = self.list[0]
        i = 1
        while True:
            if i < self.tam:
                if self.list[i].value < pivot:
                    self.menores.add(self.list[i])
                else:
                    self.maiores.add(self.list[i])
                i += 1
        if self.tam != 1:
            self.menores.quick_sort(limit)
        else:
            self.list.add(self.menores.list[0])
            self.list.add(pivot)
            self.list.add(self.maiores.list[0])
            self.list.add(self.list[0])
        if self.tam != 1:
            self.maiores.quick_sort(limit)
        else:
            self.list.add(self.maiores.list[0])
            self.list.add(pivot)
            self.list.add(self.maiores.list[0])
def main():
    """#"""
    times = int(input())
    limit = int(input())
    lista_estatica = LE(times-1)
    for _ in range(times-1):
        lista_estatica.add(int(input()))
    lista_estatica.quick_sort(limit)
    lista_estatica.show()

if __name__ == '__main__':
    main()
