male(john).
female(sussan).
parent(sussan,john).

mother(X,Y):- female(X),male(Y),parent(X,Y).
