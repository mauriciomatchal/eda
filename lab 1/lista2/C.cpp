#include <iostream>
#include <string>

using namespace std;

int main() {
    int sum = 0, amount = 0, prev, max, min, num;
    while(true) {
        string entrada;
        cin >> entrada;
        
        if(entrada == "FIM") {
            if (amount > 0) {
                int media = sum / amount;
                cout << media << endl;
                
                sum = 0;
                amount = 0;
            }
            
            string entrada2;
            cin >> entrada2;
            
            if(entrada2 == "FIM") {
                return 0;
            } else {
                int num = stoi(entrada2);
                sum += num;
                amount += 1;
            }
        } else {
            if (num < stoi(entrada)) {
                min = num;
            } else {
                max = num;
            }
            num = stoi(entrada);
            sum += num;
            amount += 1;
        } 
    }
    return 0;
}