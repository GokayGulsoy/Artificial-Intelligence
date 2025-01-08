pred(A,'asia capital'):-
	capital(A,B),asia(B),write(A),nl.
	
capital(india,delhi).
asia(delhi):-write('PM Modi is Best'),nl.

owned(B,A):-owns(A,B),cat(B),write(A),nl.
owns(james,sphynx).
cat(sphynx).
