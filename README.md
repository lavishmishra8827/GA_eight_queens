# GA_eight_queens
This is the use of genetic algorithms to solve eight queens on a chessboard problem.

Problem:-
  The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the more general n queens problem of placing n non-attacking queens on an n×n chessboard, for which solutions exist for all natural numbers n with the exception of n = 2 and n = 3.
  
 Solution:-
  I am taking a random generation of a chessboard representation of size 8(configurable). Then I have written corresponding Genetic Algorithm logic which uses crossover and mutations principles between fittest parents to generate a more fit offspring and hence improving the fitness of population by the criteria 'Selection of the fittest'. This is repeatedly carried out such that the fitness of the population keeps increasing and after some generations, we get correct solution of the problem.
  
  Fitness function definition used:
    For a particular chess board representation, fitness score, I have assigned is the total number of queens, not intersecting with others in any possible way.
