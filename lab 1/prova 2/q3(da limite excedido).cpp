#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int figurinhas, i, consultas;
    cin >> figurinhas;
    vector<int> ids;
    vector<int> quantidades;

    for (i = 0; i < figurinhas; i++) {
        cin >> ids[i];
    }
    for (i = 0; i < figurinhas; i++) {
        cin >> quantidades[i];
    }

    cin >> consultas;
    
    for (i = 0; i < consultas; i++) {
        int troca;
        cin >> troca;
        if (find(ids.begin(), ids.end(), troca) == ids.end()) {
            cout << "Quero" << endl;
        } else {
            if (quantidades[troca] == 1) {
                
            }
        }
    }
    for (int troca : trocas) {
        if (find(ids.begin(), ids.end(), troca) == ids.end()) {
            cout << "Quero" << endl;
        } else if (find(ids.begin(), ids.end(), troca) != ids.end()) {
            int savei = 0;
            for (int x : ids) {
                if (x == troca) {
                    break;
                } else {
                    savei++;
                }
            }
            if (quantidades[savei] == 1) {
                cout << "Apenas uma" << endl;
            } else {
                cout << "Trocar" << endl;
            }
        }
    }
    return 0;
}