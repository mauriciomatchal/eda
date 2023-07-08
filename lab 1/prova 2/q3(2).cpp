#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstdio>

using namespace std;

int main() {
    int figurinhas, consultas, i;
    
    unordered_map<int,int> aaa;
    vector<int> ids;
    vector<int> quantidades;

    cin >> figurinhas;

    ids.resize(figurinhas);
    quantidades.resize(figurinhas);

    for (i = 0; i < figurinhas; i++) {
        cin >> ids[i];
    }
    for (i = 0; i < figurinhas; i++) {
        cin >> quantidades[i];
    }
    for (i = 0; i < figurinhas; i++) {
        aaa[ids[i]] = quantidades[i];
    }

    cin >> consultas;
    for (i = 0; i < consultas; i++) {
        int index = 0;
        cin >> index;

        /*Se tiver a figurinha*/
        if (aaa.find(index) != aaa.end()) {
            /* Se for 1 */
            if (aaa[index] == 1) {
                printf("Apenas uma\n");
            } else {
                printf("Trocar\n");
            }
        } else {

            /* Não achou a figurinha */
            printf("Quero\n");
        }
        index = 0;
    }
    
    return 0;
}
