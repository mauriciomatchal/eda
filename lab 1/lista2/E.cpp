#include <iostream>

using namespace std;

int main() {
    int score, sumEven, sumOdd, num;
    cin >> score;

    for(int i = 0; i < score; i++) {
        cin >> num;
        if(i % 2 == 0) {
            sumEven += num;
        } else {
            sumOdd += num;
        }
    }
    if(sumEven > sumOdd) {
        cout << "Vou ajudar" << endl;
    } else {
        cout << "Modo Hard" << endl;
    }
    return 0;
}