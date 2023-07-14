#include <iostream>

using namespace std;

int main() {
    int input;
    cin >> input;
    int div[input];

    for (int i = 0; i < input; i++) {
        cin >> div[i];
    }

    for (int x : div) {
        int b;
        cin >> b;
        if (b == 0) {
            cout << "0 ";
        } else {
            float calculo;
            calculo = (b * 100) / x;
            cout << calculo << " ";
        }
    }
    cout << endl;

    return 0;
}
