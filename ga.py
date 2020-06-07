import random
import numpy

# define random based cross over
def cross_over(solutions):
    # create random variables for cross over action
    x = random.randint(0, len(solutions) - 1)
    y = random.randint(0, len(solutions) - 1)
    # choose solutions from solutions randomly
    solution1 = solutions[x]
    solution2 = solutions[y]
    length = int(len(solution1) / 2)
    # perform cross over and return
    return solution1[0:length], solution2[length:len(solution2)]


def slaves(masters):
    # create slaves and if it is necessary perform mutation
    slaves = []  # create slave array
    for i in range(0, len(masters) - 2, 3):
        # perform mutation if necessary
        if random.random() < mutation_rate:
            re_slaves = masters[i:i + 3]  # create a new children from parents
            fitness_value = [fitness_function(sol) for sol in re_slaves]  # store fitness values into an array
            re_slaves.pop(fitness_value.index(min(fitness_value)))  # pop the children who has minimum fitness value
            re_slave = mutation(re_slaves[random.randint(0, 1)])  # create a new child with mutation
            re_slaves.append(re_slave)  # add this child to the children
            slaves.extend(re_slaves)  # add these children to children
        else:
            slaves.extend(masters[i:i + 3])  # add children to children from parents
    return slaves  # return children


def mutation(solution):
    # define a random based mutation between the random solutions
    newsolution = solution[:]
    x = 0
    y = 0
    while x == y:
        x = random.randint(0, len(solution) - 1)
        y = random.randint(0, len(solution) - 1)
    newsolution[x], newsolution[y] = newsolution[y], newsolution[x]  # mutate by swapping random solutions
    return newsolution  # return mutated solutions


def fitness_function(solution):
    # in this function we need to check diagonal collisions of queen occupies
    n = len(solution)
    value = (n - 1) * n  # define fitness value
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                # if it two queens are next to each other or diagonally align decrease value by 1
                if i - solution[i] == j - solution[j] or i + solution[i] == j + solution[j]:
                    value -= 1
    return value / 2  # return fitness value


# print the board
def print_board(board):
    for row in board:
        print(" ".join(row))


def queen_input():
    # takes number of queens
    n = int(input('Enter the number of queens '))
    if n <= 3:
        print("Value should be greater than or equal to 4")
    return n

while True:
    # Variable Definition
    crossover_rate = 0.8;  # determine a crossover rate
    mutation_rate = 0.5  # determine a mutation rate
    nq = queen_input()  # take the number of queens as an input
    solutions = []
    size = nq * 3  # determine a solution size
    gen_limit = nq * nq * nq  # determine a generation limit
    max_fitness = nq * (nq - 1) / 2  # define the maximum fitness value
    for i in range(size):
        solutions.append(random.sample(range(nq), nq))
    sol_fitness = [fitness_function(sol) for sol in solutions]
    j = 0
    solution_exists = False  # define a boolean flag for the below loop
    while j < gen_limit:
        # if necessary do the cross over
        if random.random() < crossover_rate:
            cross_over(solutions)
        for i in range(len(sol_fitness)):
            if sol_fitness[i] == max_fitness:  # if chromosome has the maximum fitness value then print
                print(solutions[i])
                board = []  # create the board
                for x in range(nq):
                    board.append(["x"] * nq)  # Mark empty cells with "X"
                for k in range(nq):
                    board[solutions[i][k]][k] = "Q"  # Mark queen cells with "Q"
                print_board(board)  # print the board
                solution_exists = True
                break
        else:
            # print the generation maximum fitness value and sum of the fitness values
            print('Generation {}: Max Fitness {}: Sum Fitness {}'.format(j, max(sol_fitness), sum(sol_fitness)))
            j += 1  # increase the generation in every iteration
        if solution_exists:  # if an appropriate solution is found then break
            break
        prob = [x / sum(sol_fitness) for x in sol_fitness]  # probability for the random sample below
        # create a random sample for masters
        master_sample = numpy.random.choice([i for i in range(size)], size=size, p=prob)
        masters = [solutions[i] for i in master_sample]
        # use slaves function to create slaves and assign them in to solutions array
        solutions = slaves(masters)
        sol_fitness = [fitness_function(sol) for sol in solutions]

    if not solution_exists:
        # if no solution is found print the message
        print("Couldn't find an appropriate solution in this random process. You should try until you get an solution.")
