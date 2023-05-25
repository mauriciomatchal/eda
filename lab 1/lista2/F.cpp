#include <iostream>

using namespace std;

int main() {
    int missao, xp, yoda, luke, asoka;
    cin >> missao >> xp;

    cin >> yoda >> luke >> asoka;

    int soma = missao * xp;
    yoda += soma;
    luke += soma;
    asoka += soma;

    cout << "Yoda " << yoda << endl;
    cout << "Luke " << luke << endl;
    cout << "Ahsoka " << asoka << endl;

    return 0;
}