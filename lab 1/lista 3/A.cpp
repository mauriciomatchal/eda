#include <iostream>

using namespace std;

int main() {  
    int num, max = 0, checker;
    while (true) {
        cin >> num;  
        max = num/2;
        checker = 0;
        if (num == 0) {
            return 0;
        } else if (num == 1) {
            cout << "O numero de cadeiras nao eh primo!" << endl;
            continue;
        }  
        for (int i = 2; i <= max; i++) {  
            if (num % i == 0) {  
                checker = 1;
            }  
        }  
        if (checker == 0) {
            cout << "O numero de cadeiras eh primo!" << endl;
        } else {
            cout << "O numero de cadeiras nao eh primo!" << endl;
        } 
    }  
    return 0;

}  