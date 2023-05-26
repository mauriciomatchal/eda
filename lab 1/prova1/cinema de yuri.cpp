#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int capacidade, ocupados;

    cin >> capacidade;
    cin >> ocupados;
    vector<int> lugares; // {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    for(int i = 1; i <= capacidade; i++) {
        lugares.push_back(i);
    }

    vector<int> lugaresOcupados; // {1, 2, 3, 5, 6, 7}

    for(int i = 0; i < ocupados; i++) {
        int lugar;
        cin >> lugar;
        lugaresOcupados.push_back(lugar);
    }
    if(ocupados > 0) {
        for(int x : lugares) {
            if (find(lugaresOcupados.begin(), lugaresOcupados.end(), x) == lugaresOcupados.end()) {
                cout << x << " ";
            }
        }
    } else {
        for(int x : lugares) {
            cout << x << " ";
        }
    }


    return 0;
}