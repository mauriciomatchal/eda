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
    def selection_sort(self, limit):
        """#"""
        used_limit = 0
        for i in range(self.tam - 1):
            lower = i
            if used_limit < limit:
                for x in range(i + 1, self.tam):
                    if self.list[x].value < self.list[lower].value:
                        lower = x
                self.list[i], self.list[lower] = self.list[lower], self.list[i]
                used_limit += 1
            else:
                break
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
    lista_estatica.selection_sort(limit)
    lista_estatica.show()
if __name__ == '__main__':
    main()
