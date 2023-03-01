#include <iostream>

using namespace std;

const string WANDO = "Wando";
const string EDER = "Eder";

void imprimir( int ganhador ) {
  if ( ganhador % 2 ) cout << WANDO;
  else cout << EDER;
}

int particao( int seq[ ], int inicio, int fim, int& mexidas ) {
  int i = inicio;
  int j = fim;
  int pivot = seq[inicio];

  while ( i < j ) {
    while ( seq[i] < pivot )
      i++;

    while ( seq[j] > pivot )
      j--;

    if ( i < j ) {
      swap( seq[i], seq[j] );
      i++;
      j--;
      mexidas++;
    }
  }

  return j;
}

void quickSort( int seq[ ], int inicio, int fim, int& mexidas ) {
  if ( inicio < fim ) {
    int p = particao( seq, inicio, fim, mexidas );
    quickSort( seq, inicio, p, mexidas );
    quickSort( seq, p + 1, fim, mexidas );
  }
}

int jogo( int seq[ ], int inicio, int fim ) {
  int mexidas = 0;
  quickSort( seq, inicio, fim, mexidas );
  return mexidas;
}

int main() {
  int n;
  bool primeiro = true;

  while ( cin >> n ) {
    if ( primeiro ) primeiro = false;
    else cout << endl;

    int seq[n];
    for ( int i = 0; i < n; i++ )
      cin >> seq[i];

    imprimir( jogo( seq, 0, n - 1 ) );

  }

  return 0;
}