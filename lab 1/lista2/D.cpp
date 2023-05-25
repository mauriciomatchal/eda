#include <iostream>

using namespace std;

int main() {
    int amount;
    cin >> amount;
    int parts[amount];
    int mult;

    for(int i = 0; i < amount; i++) {
        cin >> parts[i];
    }
    cin >> mult;
    for(int i = 0; i < amount; i++) {
        parts[i] = parts[i] * mult;
        cout << parts[i] << " ";
    }
    return 0;
}