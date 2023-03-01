/*
  202011125 - Danilo Aparecido Namitala
  201820005 - Diego Marques Andrade
  201820274 - Rafael Porto Vieira de Moura
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#define DECRESCENT  greater<int>()
#define CRESCENT less<int>()

int planejamento( int motoristas, int horas, int valor ) {
  vector<int> matutinas( motoristas );
  vector<int> vespertinas( motoristas );

  for ( int i = 0; i < motoristas; i++ ) {
    cin >> matutinas[i] >> vespertinas[i];
  }

  sort( matutinas.begin(), matutinas.end(), DECRESCENT );
  sort( vespertinas.begin(), vespertinas.end(), DECRESCENT );

  int solucao[motoristas + 1];
  solucao[0] = 0;
  for ( int m = 0; m < motoristas; m++ ) {

    int soma_das_rotas = vespertinas.back() + matutinas[m];
    vespertinas.pop_back();

    int excedente = soma_das_rotas - horas;

    int s = m + 1;
    solucao[s] = excedente > 0 ? excedente * valor : 0;
    solucao[s] += solucao[s - 1];
  }


  int resposta = solucao[motoristas];
  return resposta;
}

int main() {
  int motoristas, horas, valor;

  cin >> motoristas >> horas >> valor;
  while ( motoristas && horas && valor ) {
    cout << planejamento( motoristas, horas, valor );
    cin >> motoristas >> horas >> valor;
    if ( motoristas && horas && valor ) cout << endl;
  }
  return 0;
}
