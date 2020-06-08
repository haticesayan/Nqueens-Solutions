# Nqueens Problem
This problem is about finding an arrangement of N queens on a chess board, such that no queen can attack any other queens on the board.
The chess queens can attack in any direction as horizontal, vertical, and diagonal way.
## N QUEENS PROBLEM WITH BACKTRACKING
- Place the queens column wise, start from the left most column
- If all queens are placed.
- return true and print the solution matrix.
- Else
- Try all the rows in the current column.
- Check if queen can be placed here safely if yes mark the current cell in solution matrix as Q and try to solve the rest of the problem recursively.
- If placing the queen in above step leads to the solution return true.
- If placing the queen in above step does not lead to the solution , BACKTRACK, mark the current cell in solution matrix as X and return false.
- If all the rows are tried and nothing worked, return false and print NO SOLUTION.
## N QUEENS PROBLEM WITH GENETIC ALGORITHM
### Algorithm(masters):
- create initial population
- evaluate initial population
- run crossover operator
- create slaves
- while not done
- start slaves
- wait for slaves to finish
- run mutation operator
- end
### Algorithm(masters):
- create initial population
- evaluate initial population
- run crossover operator
- create slaves
- while not done
- start slaves
- wait for slaves to finish
- run mutation operator
- end
#### Fitness Function Idea
- For a simple method of finding conflicts:
- consider an n tuple: (q1,..., qi,..., qj ,..., qn). i-th and j-th queen share a diagonal if:
- i − qi = j − qj          
- i + qi = j + qj         
## Genetic Algorithm vs Backtracking
### MEMORY
Backtracking beats genetic algorithm in terms of memory , easy implementation. Genetic algorithm beats backtracking in terms of performance and sometimes success rate.
### DIFFICULTIES:
- In backtracking you need to wait much longer to get a solution and that can be pain.
- In genetic algorithm sometimes you need run again to get a solution and you may not always get the solution at the same amount of time.
## Solutions for where n = 8.
- BACKTRACKING:
solback
- GENETIC ALGORITHMS:

