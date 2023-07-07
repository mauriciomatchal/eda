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

    def quick_sort(self, pivot_index):
        if pivot_index < 0 or pivot_index >= self.tam:
            print('Invalid pivot index')
            return

        self._quick_sort_recursive(0, self.tam - 1, pivot_index)

    def _quick_sort_recursive(self, low, high, pivot_index):
        if low < high:
            partition_index = self._partition(low, high, pivot_index)
            self._quick_sort_recursive(low, partition_index - 1, pivot_index)
            self._quick_sort_recursive(partition_index + 1, high, pivot_index)

    def _partition(self, low, high, pivot_index):
        pivot_value = self.list[low + pivot_index].value
        i = low - 1

        for j in range(low, high + 1):
            if self.list[j].value <= pivot_value:
                i += 1
                self._swap(i, j)

        return i

    def _swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]
        
def main():
    lines = int(input())
    pivot = int(input())
    lista_estatica = LE(lines - 1)
    for _ in range(lines - 1):
        lista_estatica.add(int(input()))
    lista_estatica.quick_sort(pivot)
    lista_estatica.show()


if __name__ == '__main__':
    main()
