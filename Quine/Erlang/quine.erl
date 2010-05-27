main(_) ->
    S = "main(_) ->~n    S = ~s~n    io:format(S, [[34] ++ S ++ [34, 44]]).~n",
    io:format(S, [[34] ++ S ++ [34, 44]]).
