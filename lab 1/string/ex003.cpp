#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
    int espaco, tempo;

    cin >> espaco >> tempo;

    float velocidade = espaco/tempo;

    cout << velocidade;

    return 0;
}
