#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string tradutor(string frase) {
    vector<string> frase;

    string palavra_atual;
    string palavras;

    string resultado;

    for (char c : frase) {
        if (c != ' ') {
            palavra_atual += c;
        } else {
            palavras.push_back(c);
            palavra_atual.clear();
        }
    }




    return resultado;
}

int main() {
    string frase;
    getline(cin, frase);

    string novaFrase = tradutor(frase);
    cout << frase << endl;
    
    return 0;
}