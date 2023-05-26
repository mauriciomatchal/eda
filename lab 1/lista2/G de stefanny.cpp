#include <iostream>
#include <vector>

using namespace std;

int main() {
  int fases, vida, vidaatual, dano = 0, i;

  cin >> fases;

  vector<int> vetor(fases);
  for (i = 0; i < fases; i++) {
    cin >> vetor[i];
  }
  
  cin >> vida;
  vidaatual = vida;
  
  do {
    dano = vetor[i];
    if (vidaatual > 0) {
      if (dano == 0) {
        continue;
      }  
      else if (dano == 1) {
        vidaatual = vida;
      }
      else if (dano > vidaatual) {
        vidaatual = 0;
      } else {
        vidaatual = vidaatual - dano;        
      }
    }
    i++;
  } while (i < fases && vidaatual > 0) ;
   

  if (vidaatual > 0) {
    cout << "Yes, you can" << endl;
  } else {
    cout << "You Died" << endl;
  }
      
  return 0;
}
