#include <iostream>
using namespace std;

int main() {
/*  int number;
    cin >> number;
*/

    int c = 1;
    while (c = 1) {
        int n1, n2, n3, n4, med;
        cin >> n1 >> n2 >> n3 >> n4;
        med = (n1 + n2 + n3 + n4)/4;
        
        if(med < 7.0) {
            cout << "Perdão mo, reprovou. Badalo" << endl;
        } else {
            cout << "Não fez mais que a obrigação" << endl;
        }

        cin >> c;
    }

    return 0;
}
