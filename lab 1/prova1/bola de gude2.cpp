#include <iostream>

using namespace std;

int main() {
    int relatives, i;
    long long first, twice;
    cin >> relatives >> first;
    twice = first*2;
    
    while(i < relatives - 1) {
        twice *= 2;
        i++;
    }
    cout << twice - first << endl;

    return 0;
}