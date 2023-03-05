#include <iostream>
#include <vector>

using namespace std;

void dfs( int u, vector<vector<int>>& adj, vector<bool>& visited ) {
  visited[u] = true;
  for ( int v : adj[u] ) {
    if ( !visited[v] ) {
      dfs( v, adj, visited );
    }
  }
}

int main() {
  int n, m;
  while ( cin >> n >> m && ( n || m ) ) {
    vector<vector<int>> adj( n + 1 );
    for ( int i = 0; i < m; i++ ) {
      int u, v;
      cin >> u >> v;
      adj[u].push_back( v );
      adj[v].push_back( u );
    }

    int num_motoristas = 0;
    vector<bool> visited( n + 1, false );
    for ( int u = 1; u <= n; u++ ) {
      if ( !visited[u] ) {
        dfs( u, adj, visited );
        num_motoristas++;
      }
    }

    cout << num_motoristas << endl;
  }
  return 0;
}