import numpy as np
import sys

def show(lista, tam):
    print("***Lista***")
    for i in np.arange(tam):
        print(f'{lista[i]} ')

def insert(lista, tam, maximo, n):
    if maximo == tam:
        print("Erro: lista cheia!")
    else:
        lista[tam] = n
        tam += 1

    return tam


def main():
    MAX = int(sys.argv[1])
    TAM = 0
    lista = np.arange(MAX)
    show(lista, TAM)
    TAM = insert(lista, TAM, MAX, 10)
    TAM = insert(lista, TAM, MAX, 15)
    TAM = insert(lista, TAM, MAX, 20)
    show(lista, TAM)
    TAM = insert(lista, TAM, MAX, 25)
    show(lista, TAM)

if __name__ == '__main__':
    main()
