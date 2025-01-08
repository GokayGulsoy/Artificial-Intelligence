inter([],_,[]).

inter([H1|T1],L2,[H1|Res]):-
	member(H1,L2),
	inter(T1,L2,Res).

inter([_|T1],L2,Res):-
	inter(T1,L2,Res).

empty_list(X):-
	X = [].
	
inter_of_lists(Y,Z):- inter(Y,Z,X), !, empty_list(X).
