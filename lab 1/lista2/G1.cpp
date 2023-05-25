#include <iostream>

using namespace std;

int main() {
    int fasesAmount, vida, atual, entrada, i;

    cin >> fasesAmount;

    int fases[fasesAmount];

    for(i = 0; i < fasesAmount; i++) {
        cin >> fases[i];
    }

    cin >> vida;
    atual = vida;

    for(i = 0; i < fasesAmount; i++) {
        entrada = fases[i];
        if(atual > 0) {
            if(entrada == 1) {
                atual = vida;
            } else if(entrada > atual) {
                atual = 0;
            } else {
                atual -= entrada;
            }
        } else {
            break;
        }
    }
    
    if(atual > 0) {
        cout << "Yes, you can" << endl;
    } else {
        cout << "You Died" << endl;
    }

    return 0;
}