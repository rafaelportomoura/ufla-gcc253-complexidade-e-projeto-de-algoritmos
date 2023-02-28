/*
  202011125 - Danilo Aparecido Namitala
  201820005 - Diego Marques Andrade
  201820274 - Rafael Porto Vieira de Moura
*/

#include <iostream>
#include <cstring>

using namespace std;

typedef int quantidade_de_operandos;
typedef int numero;
#define MOD 1000000

int min( int a, int b ) {
  return a < b ? a : b;
}

int calcula( numero n, quantidade_de_operandos x ) {
  int s[n + 1][x + 1];

  memset( s, 0, sizeof( s ) );

  for ( int i = 0; i <= n; i++ ) {
    s[i][1] = 1;
  }
  for ( int j = 0; j <= x; j++ ) {
    s[0][j] = 1;
  }

  s[0][0] = 1;
  for ( int i = 1; i <= n; i++ ) {
    for ( int j = 2; j <= x; j++ ) {
      for ( int k = 0; k <= i; k++ ) {
        s[i][j] = ( s[i][j] + s[k][j - 1] ) % MOD;
      }
    }

  }
  return s[n][x];
}

int main() {
  numero n;
  quantidade_de_operandos x;

  cin >> n >> x;

  while ( n || x ) {
    cout << calcula( n, x );
    cin >> n >> x;
    if ( n || x ) cout << endl;
  }
  return 0;
}