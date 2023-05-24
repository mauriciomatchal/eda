#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    // ordenar as músicas por odem alfabetica -> pesquisar como fazer isso
    int amount;
    cin >> amount;
    cin.ignore();
    string list[amount]; // creates a list

    for(int i = 0; i < amount; i++) {
        getline(cin, list[i]);
    } // appends the values of the sequence of inputs

    sort(list, list + amount);

    for(int i = 0; i < amount; i++) {
        cout << list[i] << endl;
    } // prints out the sorted list
    
    return 0;
}
