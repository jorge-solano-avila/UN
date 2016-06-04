//LAGRANGE
x = [4; 5]
y = [0.1163 0.1350]
n = length( x )
L = [1; 1; 1]
for j = 1: n
	k = j
	L( j ) = poly( [1], "x", "c" );
	deno = 1;
	for i = 1: n
		if i ~= k
			//disp( poly( [x( i )], "x" ) )
			L( j ) = L( j ) * poly( [x( i )], "x" );
			//disp( L( j ) )
			deno = deno * ( x( k ) - x( i ) );
		end
	end
	L( j ) = L( j ) / deno
end

result = 0

L = L * y

for i = 1: n
	result = result + L( i, i )
end

disp( result )

clf()

xx = ( x( 1 ): 0.25: x( n ) )
yy = horner( result, xx )

plot( xx', yy' )

xtitle( "LAGRANGE", "x" )
