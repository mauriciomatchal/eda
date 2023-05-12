#include <iostream>
using namespace std;

int main() {
    int x, y;

    cin >> x >> y;

    int x_, y_;

    cin >> x_ >> y_;

    if (x == x_ && y == y_) {
        cout << "Soltar pacote" << endl;
    } else {
        cout << "Nao soltar pacote" << endl;
    }

    return 0;
}