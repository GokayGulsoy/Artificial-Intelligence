/* Recursively processing data */
go:- loop(start).  
    loop(end).   
    loop(A) :- A\=end, write('The value is: '), read(Word),  
    write('Input value is '), write(Word), nl, loop(Word).

/* same functionality with disjunction (;) */
loop:- write('The value is: '), read(Word),
       write('Input value is: '), write(Word),nl,
       (Word=end;loop).
       

/* Recursively asking question until correct answer is provided*/       
get_answer(Answer):- write('Enter answer to question'),
		     nl,get_answer1(Answer).								

get_answer1(Answer):- write('yes or no answer: '),       
       		      read(X),	
       		      ((valid(X),Answer=X,write('The correct answer is: '),
       		      write(X),nl);get_answer1(Answer)).
       		      valid(yes).
       		      valid(no).
       		      
/* repeat built-in predicate for looping */       		      
get_answer2(Answer):- 
		write('Enter answer to question'),nl,
		repeat, write('yes or no answer: '),read(Answer),
		valid2(Answer),
		write('The correct answer is: '),write(Answer),nl.
		valid2(yes).
		valid2(no).

