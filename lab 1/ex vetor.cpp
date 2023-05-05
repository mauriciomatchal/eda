#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int list[10];

    for(int i = 0; i < 10; i++) {
        cin >> list[i];
    }
    for (int i = 0; i < 10; i++) {
        cout << list[i] << " ";
    }
    cout << endl;

    return 0;
}
