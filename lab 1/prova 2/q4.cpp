#include <iostream>
#include <vector>

using namespace std;

int main() {
    int corridas, res = 0, chave;
    cin >> corridas;
    vector<int> indices;
    vector<int> resp;
    for (int i = 0; i < corridas; i++) {
        int cavalos;
        cin >> cavalos;
        for (int i = 0; i < cavalos; i++) {
            int indice;
            cin >> indice;
            indices.push_back(indice);
        }
        cin >> chave;
        for (int x : indices) {
            if (x == chave) {
                break;      
            } else {
                res++;
            }
        }
        resp.push_back(res);
        res = 0;
        indices.clear();
    }
    
    for (const int& x : resp) {
        cout << x << endl;
    }
    
    return 0;
}