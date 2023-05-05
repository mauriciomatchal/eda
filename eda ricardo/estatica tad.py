import numpy as np

class No:
    def __init__(self, v):
        self.valor = v

    def show(self):
        return(f'Valor: {self.valor}')

class Lista:
    def __init__(self, m):        
        self.tam = 0   
        self.MAX = m
        self.lista = np.empty(m, No)
    
    def insert(self, v):
        if self.tam < self.MAX:
            n = No(v)
            self.lista[self.tam] = n
            self.tam += 1
        else:
            print('Erro! Lista cheia!')

    def show(self):
        print("***Lista***")
        for i in np.arange(self.tam):
            print(f'{i}: {self.lista[i].show()}')


def main():
    l = Lista(3)
    l.show()
    l.insert(10)
    l.insert(15)
    l.insert(20)
    l.show()
    l.insert(25)
    l.show()

if __name__ == '__main__':
    main()