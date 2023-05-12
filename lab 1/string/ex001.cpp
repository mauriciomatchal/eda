#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    float base_maior, base_menor, altura;

    cin >> base_maior;
    cin >> base_menor;
    cin >> altura;
    
    float area = ((base_maior + base_menor) * altura)/2;

    cout << fixed << setprecision(1) << "A=" << area << endl;

}