/* Loopin mechanism is implemented by recursion in Prolog */
loop(0).
loop(N):- N>0,write('value of N is: '),write(N),nl,
S is N-1,loop(S).


output_finish_message(First_value,Last_value):- First_value =:= Last_value,nl, write('Finished iteration'),nl.

output_value(First_value,Last_value):- 					   			write(First_value),output_finish_message(First_value,Last_value).

continue_iteration(First_value,Last_value):-
First_value =\= Last_value,nl,N is First_value+1,output_values(N,Last_value).

output_values(First_value,Last_value):- output_value(First_value,Last_value); continue_iteration(First_value,Last_value).

/* sum of integers from 1 to N inclusive */  
sumto(1, 1).  
sumto(N, M) :- N>1, N1 is N-1, sumto(N1, M1), M is M1+N.

read_six_lines(Infile):-see(Infile),process_terms(6),seen.

process_terms(0).
process_terms(N):- N>0, read(A),write(A),nl,N1 is N-1,process_terms(N1).

