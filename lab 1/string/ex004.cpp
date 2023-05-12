#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
    int total, frente, direita, esquerda, atras;

    cin >> total >> frente >> direita >> esquerda >> atras;

    int resposta = total - (frente + direita + esquerda + atras);

    cout << resposta << endl;


    return 0;
}