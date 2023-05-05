#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int vector[10];

    for(int i = 0; i < 10; i++) {
        cin >> vector[i];
    }
    for (int i = 0; i < 10; i++) {
        cout << vector[i] << " ";
    }
    cout << endl;

    return 0;
}
