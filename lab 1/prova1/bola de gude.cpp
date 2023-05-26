#include <iostream>

using namespace std;

int main() {
    int familiares;
    long long primeiraBola, sum = 0;
    cin >> familiares >> primeiraBola;

    for(int i = 0; i < familiares; i++) {
        if(i == familiares - 1) {
            sum += primeiraBola;
        } else {
            sum += primeiraBola;
            //cout << sum << endl;
            primeiraBola *= 2;
            //cout << primeiraBola << endl;
        }
    }
    cout << sum << endl;
    return 0;
}