#include <iostream>
#include <vector>

using namespace std;


bool DEBUG = false;

void log( string x, bool should_log = true, bool verbose = DEBUG ) {
  if ( verbose && should_log ) cout << x;
}

int funcao( int soma_das_rotas, int horas ) {
  return soma_das_rotas < horas ? horas - soma_das_rotas : soma_das_rotas - horas;
}

bool retornaMelhor( int old, int actual, int horas ) {
  int f_old = funcao( old, horas );
  int f_actual = funcao( actual, horas );

  return f_old < f_actual ? false : true;
}



int planejamento( int motoristas, int horas, int valor ) {
  vector<int> matutinas( motoristas );
  vector<int> vespertinas( motoristas );

  for ( int i = 0; i < motoristas; i++ ) {
    cin >> matutinas[i] >> vespertinas[i];
  }


  int solucao[motoristas];

  for ( int m = 0; m < motoristas; m++ ) {
    int melhor = INT32_MAX;
    int index_melhor = -1;
    for ( int v = 0; v < ( int )vespertinas.size(); v++ ) {
      int soma_das_rotas = matutinas[m] + vespertinas[v];

      log( "\t" );
      log( to_string( matutinas[m] + vespertinas[v] ), true );
      log( to_string( matutinas[m] ), false );
      log( to_string( vespertinas[v] ), false );
      if ( retornaMelhor( melhor, soma_das_rotas, horas ) ) {
        melhor = soma_das_rotas;
        index_melhor = v;
      }
    }
    if ( index_melhor >= 0 ) {
      vespertinas.erase( vespertinas.begin() + index_melhor );
    }
    log( "\t" + to_string( vespertinas.size() ) + "\n" );
    solucao[m] = melhor > horas ? ( melhor - horas ) * valor : 0;
    if ( m > 0 )
      solucao[m] += solucao[m - 1];
  }


  int resposta = solucao[motoristas - 1];
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
