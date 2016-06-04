function y = func1( x )
y = 0.95 * x.^ 5 - 3 * x. ^ 4 + 12.5 * x - 9.5 + 0.953 * cos( 10 ^ ( -8 ) * x );
endfunction

plot( -100:100, func1 )

x0 = 0.3;
xi = 0.4;
et = 0.00001;
i = 0;
f0 = func1( x0 )
fi = func1( xi ) 
while abs( fi ) > et
    temp = xi;
    xi = xi - ( ( fi * ( x0 - xi ) ) / ( f0 - fi ) );
    x0 = temp;
    f0 = fi;
    fi = func1( xi ); 
    i = i + 1;
    [i, xi, fi]
end;
