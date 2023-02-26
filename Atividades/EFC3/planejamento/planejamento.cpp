#include <iostream>

using namespace std;

int min( int a, int b ) {
  return  a < b ? a : b;
}

int funcao( int horas, int soma_das_rotas ) {
  if ( soma_das_rotas > horas ) {
    return soma_das_rotas - horas;
  }
  else {
    return horas - soma_das_rotas;
  }
}

int calcula( int matutinas[ ], int vespertinas[ ], int motoristas, int horas, int valor ) {
  int matrix[motoristas][motoristas];
  int solucao[motoristas];

  for ( int matutina = 0; matutina < motoristas; matutina++ ) {
    for ( int vespertina = 0; vespertina < motoristas; vespertina++ ) {
      matrix[matutina][vespertina] = matutinas[matutina] + vespertinas[vespertina];
      cout << "\t" << matrix[matutina][vespertina];
    }
    cout << endl;
  }
}


int planejamento( int motoristas, int horas, int valor ) {
  int matutinas[motoristas];
  int vespertinas[motoristas];

  for ( int i = 0; i < motoristas; i++ ) {
    cin >> matutinas[i] >> vespertinas[i];
  }

  return calcula( matutinas, vespertinas, motoristas, horas, valor );
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
