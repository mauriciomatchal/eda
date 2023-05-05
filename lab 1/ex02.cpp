#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float price;
    int origin;

    cout << "Fale o preço: " << endl;
    cin >> price;

    cout << "Fale a origem: " << endl;
    cin >> origin;

    switch (origin) {
        case 1:
            cout << "A região: Sul, e o preço? R$" << fixed << setprecision(2) << price << endl;
            break;
        case 2:
            cout << "A região: Norte, e o preço? R$" << fixed << setprecision(2) << price << endl;
            break;
        case 3:
            cout << "A região: Nordeste, e o preço? R$" << fixed << setprecision(2) << price << endl;
            break;
        case 4:
            cout << "A região: Centro-Oeste, e o preço? R$" << fixed << setprecision(2) << price << endl;
            break;
        case 5:
            cout << "A região: Sudeste, e o preço? R$" << fixed << setprecision(2) << price << endl;
            break;
        default:
            cout << "O Brasil só tem 5 regiões, deixe de ser burro" << endl;
            break;
    }

    return 0;
}
