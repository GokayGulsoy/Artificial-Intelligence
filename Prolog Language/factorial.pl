/* Factorial Problem */

factorial(0,1).

factorial(N,F):-
	N>0,
	N1 is N-1,
	factorial(N1,F1),
	F is N * F1.
	
	
/* Another way to compute factorial */	
factorial2(0,F,F).	
	
factorial2(N,A,F):-
	N>0,
	A1 is N*A,
	N1 is N-1,
	factorial2(N1,A1,F).	
