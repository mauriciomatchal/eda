#include <iostream>

using namespace std;

int main() {
    int maestrias[6], sum = 0;

    for(int i = 0; i < 6; i++) {
        int maestria;
        cin >> maestria;
        sum += maestria;
    }

    if(sum >= 250) {
        cout << "S+" << endl;
    } else if(sum >= 200) {
        cout << "S" << endl;
    } else if(sum >= 180) {
        cout << "S-" << endl;
    } else if(sum >= 150) {
        cout << "A+" << endl;
    } else if(sum >= 100) {
        cout << "A" << endl;
    } else if(sum >= 80) {
        cout << "A-" << endl;
    } else if(sum >= 60) {
        cout << "B+" << endl;
    } else if(sum >= 40) {
        cout << "B" << endl;
    } else {
        cout << "B-" << endl;
    }

    return 0;
}