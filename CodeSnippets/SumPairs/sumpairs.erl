-module(sumpairs).
-export([sumpairs/1]).

sumpairs([X,Y|T]) -> [X+Y | sumpairs([Y|T])];
sumpairs([_]) -> [].
