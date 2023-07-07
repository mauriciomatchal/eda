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
    def bubble_sort(self, limit):
        used_limit = 0
        #limit = 3
        #for x in range(limit):
        while True:
            if used_limit < limit:
                #sorts the bigger number to the end
                i = 0
                while True:
                    if i < self.tam - 1:
                        if self.list[i].value > self.list[i+1].value:
                            self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
                            i += 1
                        else:
                            i += 1
                    else:
                        used_limit += 1
                        break
            else:
                break
                    
                 
            
        

def main():
    """#"""
    times = int(input())
    limit = int(input())
    lista_estatica = LE(times-1)
    for _ in range(times-1):
        lista_estatica.add(int(input()))
    lista_estatica.bubble_sort(limit)
    lista_estatica.show()
if __name__ == '__main__':
    main()
