dog(pug).
dog(boxer).
dog(rottweiler).

alldogs:- dog(A),write(A),write('is a dog'),nl,fail.
alldogs.

person(tom,cruise,teacher,australia,45).
person(johnny,depp,teacher,colombia,38).
person(tom,cruise,engineer,australia,30).
person(vin,diesel,actor,brazil,41).

allteachers:- person(FirstName,LastName,teacher,_,_),
	      write(FirstName),write(' '),write(LastName),nl,
	      fail.
allteachers.



