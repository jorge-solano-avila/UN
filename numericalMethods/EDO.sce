clc;
disp(" ** Laboratorio 6 / - Grupo 7 ** ");
disp("Codigos: 2879620 02215757 223673");
ww=getdate();
mprintf( "AA:%d ,MM:%d ,DD:%d a las HH:%d ,MM:%d ,SS:%d ",ww(1),ww(2),ww(6),ww(7),ww(8),ww(9));

function y2 = f( x, y )
    y2 = -20 * x - 200 * y;
endfunction

function F = rks4Op( x0, y0, h, n )
    F = zeros( 1, 9 );
    xi = x0;
    yi = y0;
	k1 = 0;
	k2 = 0;
	k3 = 0;
	k4 = 0;
	g1 = 0;
	g2 = 0;
	g3 = 0;
	g4 = 0;
    for i = 1 : n
    	k1 = h * f( xi, yi );
        g1 = f( xi, yi );
        k2 = h * f( xi + h / 2, yi + k1 / 2 );
        g2 = f( xi + h / 2, yi + k1 / 2 );
        k3 = h * f( xi + h / 2, yi + k2 / 2 );
        g3 = f( xi + h / 2, yi + k2 / 2 );
        k4 = h * f( xi + h, yi + k3 );
        g4 = f( xi + h, yi + k3 );
        xi = xi + h;
        yi = yi + ( k1 + 2 * k2 + 2 * k3 + k4 ) / 6;
		if i == 1 then
			disp( "y1" ),
			disp( yi )
		end
    end
	disp( "f1" ),
	disp( g1 );

	disp( "f2" ),
	disp( g2 );

	disp( "f3" ),
	disp( g3 );

	disp( "f4" ),
	disp( g4 );

	disp( "g1" ),
	disp( k1 );

	disp( "g2" ),
	disp( k2 );

	disp( "g3" ),
	disp( k3 );

	disp( "g4" ),
	disp( k4 );
endfunction

result = rks4Op( 0, 1, 0.01, 5 );

function r = p( t )
    r = 2;
endfunction

function r = q( t )
    r = -1;
endfunction

function a = r( t )
    a = t .^ 2 - 1;
endfunction

function [T, Z] = rks4( f1, a, b, Za, M )
    h = ( b - a ) / M;
    T = zeros( 1, M + 1 )
    Z = zeros( M + 1, length( Za ) );
    T = a : h : b;
    Z( 1, : ) = Za
    for j = 1 : M
        //deff('[z]=f(x,y)','z=x^2+y^2');
        k1 = h * feval( T( j ), Z( j, : ), f1 );
        k2 = h * feval( T( j ) + h / 2, Z( j, : ) + k1 / 2, f1 );
        k3 = h * feval( T( j ) + h / 2, Z( j, : ) + k2 / 2, f1 );
        k4 = h * feval( T( j ) + h, Z( j, : ) + k3, f1 );
        Z( j + 1, : ) = Z( j, : ) + ( k1 + 2 * k2 + 2 * k3 + k4 ) / 6;
    end
endfunction

function L = linsht( f1, f2, a, b, alpha, bet, M )
    Za = [alpha, 0];
    [T, Z] = rks4( f1, a, b, Za, M );
    U = Z( :, 1);
    Za = [0, 1];
    [T, Z] = rks4( f2, a, b, Za, M );
    V = Z( :, 1 );
    
    X = U + ( bet - U( M + 1 ) ) * V / V( M + 1 );
    L = [T' X];
endfunction

function X = trisys( A, D, C, B )
    N = length( B );
        
    for k = 2 : N
        mult = A( k - 1 ) / D( k - 1 );
        D( k ) = D( k ) - mult * C( k - 1 );
        B( k ) = B( k ) - mult * B( k - 1 );
    end
    
    X( N ) = B( N ) / D( N );
    for k = N - 1 : -1 : 1
        X( k ) = ( B( k ) - C( k ) * X( k + 1 ) ) / D( k );
        //disp( X( k ) )
    end
endfunction

function F = findiff( a, b, alpha, bet, N )
    T = zeros( 1, N + 1 );
    X = zeros( 1, N - 1 );
    Va = zeros( 1, N - 2 );
    Vb = zeros( 1, N - 1 );
    Vc = zeros( 1, N - 2 );
    Vd = zeros( 1, N - 1 );
    h = ( b - a ) / N;
    
    Vt = a + h : h : a + h * ( N - 1 );
    Vb = -h .^ 2 * r( Vt )
    Vb( 1 ) = Vb( 1 ) + ( 1 + h / 2 * p( Vt( 1 ) ) ) * alpha;
    Vb( N - 1 ) = Vb( N - 1 ) + ( 1 - h / 2 * p( Vt( N - 1 ) ) ) * bet;
    
    for i = 1 : N - 1
       Vd( i ) = 2 + h ^ 2 * q( Vt( i ) ); 
    end
    
    Vta = Vt( 1, 2 : N - 1 );
    for i = 1 : N - 2
        Va( i ) = -1 - h / 2 * p( Vta( i ) );
    end
    
    Vtc = Vt( 1, 1 : N - 2 );
    for i = 1 : N - 2
        Vc( i ) = -1 + h / 2 * p( Vtc( i ) );
    end
    
    X = trisys( Va, Vd, Vc, Vb );
    T = [a, Vt, b];
    X = [alpha, X', bet];
    F = [T; X];
endfunction

//h = 0.1
result = findiff( 0, 1, 5, 10, 10 )

disp( result )

xx = result( 1, : );
yy = result( 2, : );

realV = poly( [5 4 1], "t", "c" )

xx1 = 0 : 0.1 : 10
yy1 = horner( realV, xx1 )

disp( [xx1 ; yy1] )

plot( xx1, yy1, 'b' )
plot( xx, yy, 'r' )
xgrid
xtitle( "Gráfica t^2 + 4t + 5" )
legends(['Función';'Estimación' ],[5,2],opt="ul")

//h = 0.01
result = findiff( 0, 1, 5, 10, 100 )

xx = result( 1, : );
yy = result( 2, : );

realV = poly( [5 4 1], "t", "c" )

xx1 = 0 : 0.01 : 10
yy1 = horner( realV, xx1 )

plot( xx1, yy1, 'r', xx, yy, 'b' )
xgrid
xtitle( "Gráfica t^2 + 4t + 5" )
legends(['Función';'Estimación' ],[5,2],opt="ul")
