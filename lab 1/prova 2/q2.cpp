#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int fileiras, cadeiras;
    cin >> fileiras >> cadeiras;
    int cinema[fileiras][cadeiras];
    
    for (int i = 0; i < fileiras; i++) {
        for (int j = 0; j < cadeiras; j++) {
            cin >> cinema[i][j];
        }
    }

    for (int i = 0; i < fileiras; i++) {
        for (int j = 0; j < cadeiras - 1; j++) {
            if (cinema[i][j] == 0) {
                if (cinema[i][j+1] == 0) {
                    int savei = i+1, savej = j+1, savej2 = j+2;
                    cout << "Fileira: " << savei << endl;
                    cout << "Assentos: " << savej << " e " << savej2 << endl;
                }
            } 
        }
    }
    
    return 0;
}
