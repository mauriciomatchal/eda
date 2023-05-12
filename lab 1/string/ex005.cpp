#include <iostream>
using namespace std;

int main() {
    int range;
    cin >> range;
    int array[range];

    for (int i = 0; i < range; i++) {
        cin >> array[i];
    }

    for (int i = range - 1; i >= 0; i--) {
        cout << array[i];
    }
    cout << " " << endl;

    return 0;
}