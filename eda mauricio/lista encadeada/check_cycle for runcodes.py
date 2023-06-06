# 6
# 1 2 3 4 5 6
# 1 2
# 2 3
# 3 4
# 4 5
# 5 2
class node:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
class linked_list:
    def __init__(self):
        self.head = None
    #def create_list(self):
    
    def check_cycle(self):
        temp_1 = self.head
        temp_2 = self.head.prox
        while temp_2 is not None:
            if temp_2.prox is not None:
                if temp_1 == temp_2:
                    print('Clico')
                    return False
                    break
                if temp_2.prox is None:
                    return True
                temp_1 = temp_1.prox
                temp_2 = temp_2.prox.prox
    def set_prox(self):
        num, prox = map(int, input().split())
        if self.head is None:
            num1 = node(num)
            prox1 = node(prox)
            self.head = num1
            num1.prox = prox1
        else:
            number_mark = self.head
            direction_mark = self.head
            num1 = node(num)
            prox1 = node(prox)
            while number_mark is not None:
                if number_mark.value == num:
                    break
                number_mark = number_mark.prox
            while direction_mark is not None:
                if direction_mark.value == prox:
                    number_mark.prox = direction_mark
                    break
                if direction_mark.prox is None:
                    number_mark.prox = prox1
                direction_mark = direction_mark.prox
                
            self.check_cycle()
                
    def show(self):
        if self.head is not None:
            temp = self.head
            print('*** Lista ***')
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
         
    
    
def main():
    size = int(input())
    #list = input().split()
    lista = linked_list()
    for i in range(size - 1):
        if lista.set_prox() is False:
            break
        else:
            lista.set_prox()
    lista.show()
if __name__ == '__main__':
    main()



