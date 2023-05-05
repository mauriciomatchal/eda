#include <iostream>
using namespace std;

int main() {
    float num1, num2, num3, num4, med;

    cout << "Seu PRIMEIRO número é: " << endl;
    cin >> num1;
     
    cout << "Seu SEGUNDO número é: " << endl;
    cin >> num2;
     
    cout << "Seu TERCEIRO número é: " << endl;
    cin >> num3;
     
    cout << "Seu QUARTO número é: " << endl;
    cin >> num4;
     
    med = (num1 + num2 + num3 + num4)/4;

    cout << "Sua média é:" << med << endl;

    if (med >= 7.0) {
        cout << "Parabens!!!!! Habla" << endl;
    } else {
        cout << "Seu lixo. smt" << endl;
    } 
}

