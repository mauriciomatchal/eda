#include <iostream>
#include <iomanip>
using namespace std;


int main() {
    int number;
    cin >> number;

    for(int i = number; i >= 0; i--) {
        cout << number << endl;
        number--;
    }

    return 0;
}
