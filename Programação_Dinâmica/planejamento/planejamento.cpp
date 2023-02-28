#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#define DECRESCENT  greater<int>()
#define CRESCENT less<int>()

int funcao( int soma_das_rotas, int horas ) {
  return  soma_das_rotas - horas;
}

bool oAtualEhMelhor( int velho, int atual, int horas, int matutina ) {
  if ( atual < horas and velho < horas ) return atual > velho;

  int f_velho = funcao( velho, horas );
  int f_atual = funcao( atual, horas );


  return f_atual < f_velho;
}



int planejamento( int motoristas, int horas, int valor ) {
  vector<int> matutinas( motoristas );
  vector<int> vespertinas( motoristas );

  for ( int i = 0; i < motoristas; i++ ) {
    cin >> matutinas[i] >> vespertinas[i];
  }

  sort( matutinas.begin(), matutinas.end(), DECRESCENT );
  sort( vespertinas.begin(), vespertinas.end(), CRESCENT );

  int solucao[motoristas + 1];
  solucao[0] = 0;
  for ( int m = 0; m < motoristas; m++ ) {
    int s = m + 1;
    int melhor = INT32_MAX;
    int index_melhor = -1;

    for ( int v = 0; v < ( int )vespertinas.size(); v++ ) {
      int soma_das_rotas = matutinas[m] + vespertinas[v];

      if ( oAtualEhMelhor( melhor, soma_das_rotas, horas, matutinas[m] ) ) {
        melhor = soma_das_rotas;
        index_melhor = v;
      }
    }

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
