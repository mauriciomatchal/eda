#include <iostream>
#include <iomanip>
using namespace std;


int main() {
    float weight;
    float height;

    cin >> weight;
    cin >> height;

    float imc = weight/(height*height);
    
    if (imc < 18.5) {
        cout << "Seu IMC é: " << fixed << setprecision(2) << imc << ", e você está com baixo peso." << endl; 
    } else if (imc <= 24.9) {
        cout << "Seu IMC é: " << fixed << setprecision(2) << imc << ", e você está com peso normal." << endl; 
    } else if (imc <= 29.9) {
        cout << "Seu IMC é: " << fixed << setprecision(2) << imc << ", e você está com pré-obeso." << endl; 
    } else if (imc <= 34.9) {
        cout << "Seu IMC é: " << fixed << setprecision(2) << imc << ", e você está com obesidade I." << endl; 
    } else if (imc <= 39.9) {
        cout << "Seu IMC é: " << fixed << setprecision(2) << imc << ", e você está com obesidade II." << endl; 
    } else {
        cout << "Seu IMC é: " << fixed << setprecision(2) << imc << ", e você está com obesidade III." << endl; 
    }

    return 0;
}

