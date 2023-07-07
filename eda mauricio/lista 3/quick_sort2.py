class Node:
    def __init__(self, value):
        self.value = value

    def show_node(self):
        return f'{self.value}'


class LE:
    def __init__(self, MAX):
        self.max = MAX
        self.tam = 0
        self.list = [None] * MAX

    def show(self):
        string = ''
        for i in range(self.tam):
            string += f'{self.list[i].show_node()}' + ' '
        print(string)

    def add(self, node):
        if self.tam < self.max:
            node = Node(node)
            self.list[self.tam] = node
            self.tam += 1
        else:
            print('Full List')

    def quick_sort(self):
        self._quick_sort(0, self.tam - 1)

    def _quick_sort(self, low, high):
        if low < high:
            pivot_index = self._partition(low, high)
            
            self._quick_sort(low, pivot_index - 1)
            self._quick_sort(pivot_index + 1, high)

    def _partition(self, low, high):
        pivot = self.list[high].value
        i = low - 1

        for j in range(low, high):
            if self.list[j].value <= pivot:
                i += 1
                self.list[i], self.list[j] = self.list[j], self.list[i]

        self.list[i+1], self.list[high] = self.list[high], self.list[i+1]
        return i + 1


def main():
    times = int(input())
    limit = int(input())
    lista_estatica = LE(times - 1)
    for _ in range(times - 1):
        lista_estatica.add(int(input()))
    lista_estatica.quick_sort()
    lista_estatica.show()


if __name__ == '__main__':
    main()
