/* List and Sequence Examples */


member(A,[A|S]).
member(A,[B|S]):-member(A,S).

takeout(A,[A|S],S).
takeout(A,[F|S],[F|T]):-takeout(A,S,T).

append([A|B],C,[A|X]):-append(B,C,X).
append([],A,A).

/* Derivation 
B	C	X
list1	list2  	concatenated_list
[1,2,3]	[4,5]	[1,2,3,4,5]
1|[2,3]	[4,5]	1|[2,3,4,5]
2|[3]	[4,5]	2|[3,4,5]
3|[]	[4,5]	3|[4,5]
*/
