#include<bits/stdc++.h>

using namespace std;

int main()
{
	int n, aux;
	scanf( "%d", &n );
	vector<int> list ( n );
	for( int i = 0; i < n; i++ )
	{
		scanf( "%d", &aux );
		list.at( i ) = aux;
	}

	sort( list.begin(), list.end() );

	for( int i = 0; i < n; i++ )
		printf( "%d\n", list.at( i ) );

	return 0;	
}