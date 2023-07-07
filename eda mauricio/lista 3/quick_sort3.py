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

    def quick_sort(self, pivot):
        list_size = self.tam-1
        self._quick_sort(pivot, list_size)

    def _quick_sort(self, pivot_index, maior):
        if pivot_index < maior:
            # Choose the pivot element as the first element
            pivot = self.list[pivot_index].value
            
            i = pivot_index
            j = maior

            # Partition the list
            while i < j:
                # Move i towards the right until finding an element greater than the pivot
                while i <= maior and self.list[i].value <= pivot:
                    i += 1
                # Move j towards the left until finding an element smaller than or equal to the pivot
                while j >= pivot_index and self.list[j].value > pivot:
                    j -= 1
                if i < j:
                    # Swap the elements at indices i and j
                    self.list[i], self.list[j] = self.list[j], self.list[i]
                    
            # Move the pivot element to its correct position
            self.list[pivot_index], self.list[j] = self.list[j], self.list[pivot_index]

            # Recursively sort the partitions
            self._quick_sort(pivot_index, j - 1)
            self._quick_sort(j + 1, maior)


def main():
    times = int(input())
    pivot = int(input())
    lista_estatica = LE(times - 1)
    for _ in range(times - 1):
        lista_estatica.add(int(input()))
    lista_estatica.quick_sort(pivot)
    lista_estatica.show()


if __name__ == '__main__':
    main()
