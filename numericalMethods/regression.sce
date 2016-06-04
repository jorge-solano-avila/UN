clc;
disp(" ** Laboratorio 4 / - Grupo 7 ** ")
disp("Codigos: 2879620 02215757 223673")
ww=getdate();
mprintf( "AA:%d ,MM:%d ,DD:%d a las HH:%d ,MM:%d ,SS:%d",ww(1),ww(2),ww(6),ww(7),ww(8),ww(9));

// El resultado es A y B, donde A es la pendiente de la recta y B es el punto en el 
// eje Y donde se cruza la recta de aproximación dada por el metodo de los minimos
// cuadrados.

function [A, B] = lsline( X, Y )

xmean = mean( X );

ymean = mean( Y );

sumx2 = ( X - xmean ) * ( X - xmean )';

sumxy = ( Y - ymean ) * ( X - xmean )';

A = sumxy / sumx2;

B = ymean - A * xmean;

endfunction

clc;

X = [0.14 0.44 0.54 0.74 0.84 0.94]

Y = [0.6123 0.9223 0.9923 1.5223 1.4723 2.0323]

[A, B] = lsline( X, Y )

// Resultado de aplicar la función lsline
disp( [A B] )

regression = poly( [B A], "x", "c" )

// Polinomio de la recta aproximación
disp( regression )

y1 = horner( regression, 0.74 )

// Valor calculado de 0.74 en el polinomio aproximación
disp( y1 )

xx = ( X( 1 ) : 0.1 : X( length( X ) ) )'

yy = horner( regression, xx )'

// Gráfica del polinomio con marcas de los valores del vector X en el polinomio
plot( xx, yy )
xgrid

plot( X( 1 ), horner( regression, X( 1 ) ), 'o' )
plot( X( 2 ), horner( regression, X( 2 ) ), 'o' )
plot( X( 3 ), horner( regression, X( 3 ) ), 'o' )
plot( X( 4 ), horner( regression, X( 4 ) ), 'o' )
plot( X( 5 ), horner( regression, X( 5 ) ), 'o' )
plot( X( 6 ), horner( regression, X( 6 ) ), 'o' )

X = [0 1 2 3 4 5 6 7]
Y = [2.3 2.1 3.2 5.8 8.6 10.4 16.7 38.8]

n = length( X )

y2 = 0
for i = 1: n
	y2 = y2 + Y( i ) ^ 2
end
x2 = 0
for i = 1: n
	x2 = x2 + X( i ) ^ 2
end
x3 = 0
for i = 1: n
	x3 = x3 + X( i ) ^ 3
end
x4 = 0
for i = 1: n
	x4 = x4 + X( i ) ^ 4
end
x2y = 0
for i = 1: n
	x2y = x2y + ( X( i ) ^ 2 ) * Y( i )
end
xy = 0
for i = 1: n
	xy = xy + X( i ) * Y( i )
end
y = 0
for i = 1: n
	y = y + Y( i )
end
x = 0
for i = 1: n
	x = x + X( i )
end

A = [n x x2; x x2 x3; x2 x3 x4]
B = [y; xy; x2y]
ANS = rref( [A B] )
ANS = ANS( :, 4 )'

ANS = poly( ANS, "x", "c" )

// Polinomio de grado 2 que caracteriza la aproximación de los puntos dados
disp( ANS )

r = ( n * xy ) - ( x * y )
r = r / sqrt( ( ( n * x2 ) - ( x ^ 2 ) ) * ( ( n * y2 ) - ( y ^ 2 ) ) )

// Coeficiente de correlación
disp( r )

//-----------------Ejemplos explicativos---------------

X = [0 1 2 3 4 5 6 7]
Y = [2.3 2.1 3.2 5.8 8.6 10.4 16.7 38.8]

// Calcula la longitud del vector
n = length( X )
disp( n )

// Calcula la suma de los valores de X
n = sum( X )
disp( n )

// Calcula la suma de los cuadrados de X
n = sum( X .^ 2 )
disp( n )

// Calcula el producto entre X y Y
n = X .* Y
disp( n )

// Calcula la suma de los productos entre los valores de X y Y
n = sum( X .* Y )
disp( n )

// Calcula el producto entre X ^ 2 y Y
n = ( X .^ 2 ) .* Y
disp( n )

// Calcula la suma de los cuadrados de X multiplicados por los valores de Y
n = sum( ( X .^ 2 ) .* Y )
disp( n )

// Calcula la media de X
n = mean( X )
disp( n )

// Calcula la suma de las restas de cada valor de Y y la media de Y al cuadrado
n = sum( Y - mean( Y ) ^ 2 )
disp( n )
