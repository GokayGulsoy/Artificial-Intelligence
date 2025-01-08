/* Preventing Backtracking with cuts */
larger(X,Y,X):-X>Y,!.
larger(X,Y,Y).


sumto(1,1):-!.
sumto(N,S):-N1 is N-1, sumto(N1,S1), S is S1+N.


classify(0,zero):-!.
classify(X,negative):- X<0,!.
classify(X,positive).

go:- write(start),nl,
     repeat, write('specify a positive number: '), read(X),
     classify(X,Type),Type=positive,
     write('Positive number is '),write(X),nl.

/* Cut with Failure Example */
bird(crow).
bird(sparrow).
bird(parrot).
bird(penguins).
bird(dove).
bird(robin).
bird(turkey).
bird(hawk).
bird(goose).
bird(swallow).
bird(pigeon).
bird(woodpecker).

can_fly(penguins):-!,fail.
can_fly(A):-bird(A).
