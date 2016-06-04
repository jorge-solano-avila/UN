factorial(0,1).
factorial(2,2).
factorial(3,6).
factorial(Num,Result):-
    Num>0,
    Num1 is Num-1,
    factorial(Num1,Result1),
    Result is Num*Result1.