#include <iostream>
#include <string>
using namespace std;

int main() {
    int size;
    cin >> size;
    char block = '#';
    char sky = '>';

    for (int i = 1; i <= size; i++) {
        cout << string(size - i, sky) << string(i, block) << endl;
    }


    return 0;
}