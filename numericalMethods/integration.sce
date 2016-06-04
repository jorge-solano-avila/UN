clc;
disp("** Laboratorio 2 / - Grupo 7 ** ")
disp("Codigos: 2879620 02215757 223673")

ww=getdate();

mprintf( "AA:%d ,MM:%d ,DD:%d a las HH:%d ,MM:%d ,SS:%d",ww(1),ww(2),ww(6),ww(7),ww(8),ww(9));

function fun = fz( y, x )
    fun = ( y ^ 2 - x ^ 2 ) ^ ( 1 / 2 )
endfunction

hY = 0.5
hX = 0.25
intervalsY = 24

Y = []

for i = 1 : intervalsY + 1
    Y( i ) = ( i - 1 ) * hY - 6
end 

M = []

for i = 1 : intervalsY + 1
    limitI = ( Y( i ) ) ^ 2 - 36
    limitS = -( Y( i ) ) ^ 2 + 36
    intervalL = abs( limitI - limitS ) / hX
    if intervalL == 0 then
        M( i ) = 0
    else
        for j = 0 : intervalL
            Xl( j + 1 ) = j * hX + limitI
        end
        
        S = 0
              
        for k = 1 : ( intervalL / 2 )   
            S = S + fz( ( 36 - ( Y( i ) ) ^ 2 ), Xl( 2 * k - 1 ) ) + 4 * fz( ( 36 - ( Y( i ) ) ^ 2 ), Xl( 2 * k ) )+ fz( ( 36 - ( Y( i ) ) ^ 2 ), Xl( 2 * k + 1 ) )
        end

        M( i ) = S * ( hX / 3 )
    end
end

I = 0
for i = 1 : ( intervalsY / 2 )
    I = I + ( M( 2 * i - 1 ) + 4 * M( 2 * i ) + M( 2 * i + 1 ) );
end

I = I * ( hY / 3 )

disp( "Valor aplicando el método 1/3 de Simpson: " ),
disp( I ),

Ir = 13028.81305

disp( "Valor real del volumen: " ),
disp( Ir ),

ev = ( Ir - I ) / Ir * 100

disp( "Error relativo verdadero: " ),
disp( ev )

x = -6 : 0.5 : 6
z = -3 : 0.25 : 3

[a b] = meshgrid( x, z )

y = sqrt( b .^ 2 + a .^ 2 )

plot3d( x, z, y )

//clc

//-------------------------------------------------------

function f1 = fun1( x, h )
    f1 = ( tan( x ) - tan( x - h ) ) / h
endfunction

function f2 = fun2( x, h )
    f2 = ( tan( x + h ) - tan( x ) ) / h
endfunction

function f3 = fun3( x, h )
    f3 = ( tan( x + h ) - tan( x - h ) ) / ( 2 * h )
endfunction

function f4 = fun4( x, h )
    f4 = ( 3 * tan( x ) - 4 * tan( x - h ) + tan( x - 2 * h ) ) / ( 2 * h )
endfunction

function f5 = fun5( x, h )
    f5 = ( 2 * tan( x ) - 5 * tan( x - h ) + 4 * tan( x - 2 * h ) - tan( x - 3 * h ) ) / ( h ^ 2 )
endfunction

function error1 = e1( e )
    error1 = ( abs( 3.42551 - e ) / 3.42551 ) * 100
endfunction

function error2 = e2( e )
    error2 = ( abs( 10.66985 - e ) / 10.66985 ) * 100
endfunction

x0 = 1

h = [0.1 0.05 0.025]

result = [fun1( x0, h( 1 ) ) fun2( x0, h( 1 ) ) fun3( x0, h( 1 ) ) fun4( x0, h( 1 ) ) fun5( x0, h( 1 ) ); fun1( x0, h( 2 ) ) fun2( x0, h( 2 ) ) fun3( x0, h( 2 ) ) fun4( x0, h( 2 ) ) fun5( x0, h( 2 ) ); fun1( x0, h( 3 ) ) fun2( x0, h( 3 ) ) fun3( x0, h( 3 ) ) fun4( x0, h( 3 ) ) fun5( x0, h( 3 ) )]
disp( "   fPrima(1)    fPrima(1)    fPrima(1)    fPrima(1)  fPrimaPrima(1)" )
disp( result )

disp( "   Error 1      Error 2      Error 3      Error A      Error B" )
errors = [e1( fun1( x0, h( 1 ) ) ) e1( fun2( x0, h( 1 ) ) ) e1( fun3( x0, h( 1 ) ) ) e1( fun4( x0, h( 1 ) ) ) e2( fun5( x0, h( 1 ) ) ); e1( fun1( x0, h( 2 ) ) ) e1( fun2( x0, h( 2 ) ) ) e1( fun3( x0, h( 2 ) ) ) e1( fun4( x0, h( 2 ) ) ) e2( fun5( x0, h( 2 ) ) ); e1( fun1( x0, h( 3 ) ) ) e1( fun2( x0, h( 3 ) ) ) e1( fun3( x0, h( 3 ) ) ) e1( fun4( x0, h( 3 ) ) ) e2( fun5( x0, h( 3 ) ) );]
disp( errors )
