#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#define DECRESCENT  greater<int>()
#define CRESCENT less<int>()

int funcao( int soma_das_rotas, int horas ) {
  return soma_das_rotas < horas ? horas - soma_das_rotas : soma_das_rotas - horas;
}

bool isActualBetter( int old, int actual, int horas, int matutina ) {
  if ( matutina >= horas ) {
    return actual < old;
  }

  int f_old = funcao( old, horas );
  int f_actual = funcao( actual, horas );

  if ( f_actual == 0 ) return true;

  if ( f_actual == f_old ) return actual <= horas;

  return f_actual < f_old;
}



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
    int s = m + 1;
    int melhor = INT32_MAX;
    int index_melhor = -1;
    // cout << matutinas[m];
    for ( int v = 0; v < ( int )vespertinas.size(); v++ ) {
      int soma_das_rotas = matutinas[m] + vespertinas[v];
      // cout << "\t" << vespertinas[v];
      if ( isActualBetter( melhor, soma_das_rotas, horas, matutinas[m] ) ) {
        melhor = soma_das_rotas;
        index_melhor = v;
      }
    }
    // cout << endl;
    if ( index_melhor >= 0 ) {
      vespertinas.erase( vespertinas.begin() + index_melhor );
    }
    solucao[s] = melhor > horas ? ( melhor - horas ) * valor : 0;
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
