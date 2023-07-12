#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int sum = 0, amount = 0, num = 0, media = 0, min = 10, max = 1;
    vector<int> resultados;
    while(true) {
        string entrada;
        cin >> entrada;

        if (entrada == "FIM") {
            if (amount > 0) {
                if (amount == 1) {
                    media = num;
                    resultados.push_back(media);
                } else if (amount == 2) {
                    media = sum / 2;
                    resultados.push_back(media);
                } else {
                    media = (sum - min - max) / (amount - 2);
                    resultados.push_back(media);
                }
                sum = 0;
                amount = 0;
                min = 10;
                max = 1;
            }
            
            string entrada2;
            cin >> entrada2;
            
            if (entrada2 == "FIM") {
                break;
            } else {
                num = stoi(entrada2);
                if (num < min) {
                    min = num;
                }
                if (num > max) {
                    max = num;
                }
                sum += num;
                amount ++;
            }
        } else {
            num = stoi(entrada);
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
            sum += num;
            amount ++;
        } 
    }

    for (const int& x : resultados) {
        cout << x << endl;
    }
    
    return 0;
}