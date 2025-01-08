readterms(Infile,Outfile):-
	see(Infile),tell(Outfile),
	read(X1),write(X1),nl,read(X2),write(X2),nl,
	read(X3),write(X3),nl,read(X4),write(X4),nl,
	seen,told.
