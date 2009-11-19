sumpairs([X,Y|T],Out) :- Z is X + Y, sumpairs([Y|T], Tail), append([Z],Tail,Out).
sumpairs(_,[]).
