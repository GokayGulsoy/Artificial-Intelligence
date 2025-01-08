dog(rottweiler).
large(rottweiler).
large(siamese).
cat(siamese).
large_animal(A):-dog(A),large(A).
large_animal(C):-cat(C),large(C).
