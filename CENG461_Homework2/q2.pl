female(sussan).
male(nathan).
male(logan).
parent(logan,nathan).
parent(logan,sussan).

sister(X,Y):- parent(Z,X), parent(Z,Y), female(X).
