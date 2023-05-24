#include <iostream>

using namespace std;

int main() {
    int processo;
    cin >> processo;
    int resto = processo % 42;
    if (resto == 0) {
        cout << "Sim" << endl;
    } else {
        cout << "Nao" << endl;
    }
    return 0;
}