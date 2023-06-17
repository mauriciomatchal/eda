#include <iostream>
using namespace std;

int main() {
	int num;
	cin >> num;
    float max = num/2;
    float floor(max);
	if (num == 0) {
		return 0;
	} else if (num == 2 || num == 3 || num == 5) {
	    cout << "Seu numero é primo";
	} else {
        int i;
	    int verify = 0;
        while (i < max) {
            int rem = num % i;
        }
    }
    if(verify == 0) {
        cout << "Seu numero nao é primo";
    }
    

	return 0;
}