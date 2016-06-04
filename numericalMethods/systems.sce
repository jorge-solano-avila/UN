
// ALTERNATIVA 1
function X = backsub ( A, B )
    n = length( B );
    X = zeros( n, 1 );
    X( n ) = B( n ) / A( n, n );
    
    
    for k = n - 1: -1: 1
        X( k ) = ( B( k ) - A( k, k + 1: n ) * X( k + 1: n ) ) / A( k, k );
    end
endfunction

function X = uptrbk ( A, B )
    [N, N] = size( A );
    X = zeros( N, 1 );
    C = zeros( 1, N+1 );
    
    
    Aug = [A, B];
    
    for p = 1: N - 1
        [Y, j] = max( abs( Aug( p: N, p ) ) );
        C = Aug( p, : );
        Aug( p, : ) = Aug( j + p - 1, : );
        Aug( j + p - 1, : ) = C;
    
        if  Aug( p, p ) == 0
            break
        end
        
        for k = p + 1: N
            m = Aug( k, p ) / Aug( p, p );
            Aug( k, p: N+1 ) = Aug( k, p: N+1 ) - m * Aug( p, p: N+1 );
        end
    end
    X = backsub( Aug( 1: N, 1: N ), Aug( 1: N, N + 1 ) );
endfunction

A = [1 0 -3 0 5;0 2 -1 4 0;2 2 0 0 -5;0 0 -1 2 -1;1 1 0 0 0]
B = [17;17;21;0;3]

uptrbk( A, B )

// ALTERNATIVA 2
function X = gaussElim( A, B )
    [nA,mA] = size( A )
    [nb,mb] = size( B )
    if nA<>mA then
        error('gausselim - Matrix A must be square');
        abort;
    elseif mA<>nb then
        error('gausselim - incompatible dimensions between A and b');
        abort;
    end;
    a = [A B];

    n = nA;
    for k = 1: n - 1
        for i = k + 1: n
            for j = k + 1: n + 1
                a( i, j ) = a( i, j ) - a( k, j ) * a( i, k ) / a( k, k );
            end;
        end;
    end;

    X( n ) = a( n, n + 1 ) / a( n, n );
    for i = n - 1: -1: 1
        sumk = 0
        for k = i + 1: n
            sumk = sumk + a( i, k ) * X( k );
        end;
        X( i ) = ( a( i, n + 1 ) - sumk ) / a( i, i );
    end;
endfunction

// ALTERNATIVA 3
[L, U] = lu( A )
Y = gaussElim( L, B )
X = gaussElim( U, Y )

// ALTERNATIVA 4
ANS = [A B]
ANS = rref( ANS )
