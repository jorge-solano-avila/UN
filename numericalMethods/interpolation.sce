//LAGRANGE
x = [30.5; 50.5; 70.5; 110.5; 210.5]
y = [983 1045 1083 1137 1311]
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

//----------------------------------------------------

x = [13.5; 14.5; 15.5; 16.5; 17.5]
y = [1; 1.23607; 1.44949; 1.64575; 1.82843]
m = length( x ) - 1

//NEWTON
x = x( : )
y = y( : )
n = size( x, 1 )
DD = zeros( n, m + 1 );
DD( :, 1 ) = y;
for j = 1:m
    for i = 1:n - j
        Djfi = ( DD( i + 1, j ) - DD( i, j ) )/( x( i + j ) - x( i ) );
        DD( i , j + 1 ) = Djfi;
    end
end

//disp( DD )

coefficients = DD(1,:)

result = 0

n = length( coefficients )

for i = 2: n
	aux = 1
	for j = 1: i - 1
		temp = [-1 * x( j ) 1]
		aux = aux * poly( temp, "x", "c" )
		//disp( aux )
	end
	aux = aux * coefficients( i )
	//disp( coefficients( i ) )
	result = result + aux
end

result = result + coefficients( 1 )

disp( result )

clf()

xx = ( x( 1 ): 0.1: x( n ) )
yy = horner( result, xx )

plot( xx', yy' )

xtitle( "NEWTON", "x" )
