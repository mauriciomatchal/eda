#include <iostream>

using namespace std;

int main() {
    int x, y;
    cin >> x;
    cin >> y;

    if(x > 0 && x < 100 && y > 0 && y < 100) {
        if(x > 70 || y > 70) {
            cout << "Coordenada valida e o navio esta longe" << endl;
        } else {
            cout << "Coordenada valida e o navio esta perto" << endl;
        }
    } else {
        cout << "Coordenada invalida" << endl;
    }


    return 0;
}