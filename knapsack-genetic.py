import random
from math import pow

# total weight of the knapsack
total_weight = 0
val = []
w = []

"""
    chromosome structure: an array of binary values 
    with length of item count
    1 means that item is selected
    0 means that item is not selected
"""


def initial_chromosome_generation(population_size, chromosome_size):
    """
    Generate initial chromosomes for the population
    :param population_size:
    :param chromosome_size:
    :return:
    """
    first_generation = []
    for ch in range(population_size):
        chromosome = []
        for j in range(chromosome_size):
            chromosome.append(random.randint(0, 1))

        first_generation.append(chromosome)

    return first_generation


def fitness_function(population, population_size, chromosome_size):
    """
    Calculate fitness of each chromosome in the population
    if the it's 1 means that chromosome is selected and it's value is added to the fitness
    :param population:
    :param population_size:
    :param chromosome_size:
    :return:
    """
    global total_weight, val, w  # global variables
    current_total_weight = 0
    fitness = []
    current_fitness = 0
    for i in range(population_size):
        for k in range(chromosome_size):
            if population[i][k] == 1:
                current_fitness += val[k]
                current_total_weight += w[k]
        # if total weight of the chromosome is greater than the total weight of the knapsack that chromosome is ignored
        if current_total_weight <= total_weight:
            fitness.append(current_fitness)
        else:
            fitness.append(0)
        # reinitialize variables
        current_total_weight = 0
        current_fitness = 0
    return fitness


def selection(population, population_size, chromosome_size):
    population_fitness = fitness_function(population, population_size, chromosome_size)
    total_fitness = sum(population_fitness)
    probability = random.randint(0, total_fitness)
    selected = []
    temp_fitness_sum = 0
    for i in range(2):
        for j in range(population_size):
            temp_fitness_sum = temp_fitness_sum + population_fitness[j]
            if temp_fitness_sum >= probability:
                selected.append(population[j])
                break
        temp_fitness_sum = 0
    return selected


def crossover(first_chromosome, second_chromosome):
    """
    Crossover between two chromosomes
    select a random point to crossover
    and concatenate the two chromosomes at the selected point
    :param first_chromosome:
    :param second_chromosome:
    :return:
    """
    crossover_limit = random.randint(1, len(first_chromosome) - 1)
    crossed_chromosome = []
    new_chromosome = first_chromosome[:crossover_limit] + second_chromosome[crossover_limit:]
    crossed_chromosome.append(new_chromosome)
    new_chromosome = second_chromosome[:crossover_limit] + first_chromosome[crossover_limit:]
    crossed_chromosome.append(new_chromosome)

    return crossed_chromosome


def mutation(population):
    """
    Mutate a chromosome by randomly changing a bit
    change the bit to 1 or 0
    chance of mutation is less than 20%
    :param population:
    :return:
    """
    row_index = random.randint(0, len(population) - 1)
    col_index = random.randint(0, len(population[0]) - 1)
    mutation_rate = random.uniform(0, 1)
    if mutation_rate < 0.2:
        population[row_index][col_index] = 1 if population[row_index][col_index] == 0 else 0
    return population


if __name__ == '__main__':
    population_max_size = 100
    # mutation_rate = 0.1
    crossover_rate = 0.5
    generation_number = 0
    N = int(input("Enter number of items : "))
    val = list(map(int, input("\nEnter the values : ").strip().split()))[:N]
    w = list(map(int, input("\nEnter the weights : ").strip().split()))[:N]
    total_weight = int(input("Enter the max capacity : "))
    """
     population size is 2^N if N is less than 7
     otherwise it's 100
    """
    if pow(2, N) <= 100:
        population_size = int(pow(2, N))
    else:
        population_size = population_max_size
    # size of each chromosome is equal to the number of items
    chromosome_size = N
    population = initial_chromosome_generation(population_size, chromosome_size)

    max_number_of_generations = 100
    # reproduce generation 100 times
    while max_number_of_generations:
        generation_number += 1
        selected_population = selection(population, population_size, chromosome_size)
        crossed_population = crossover(selected_population[0], selected_population[1])
        population = population + crossed_population
        population_size += 2
        population = mutation(population)

        max_number_of_generations -= 1

    fit = fitness_function(population, population_size, chromosome_size)
    max_profit = max(fit)
    print("\nMaximum solution : ", max_profit)
    print("\nselected items : [", end="")
    index = fit.index(max_profit)
    for i in range(chromosome_size):
        if population[index][i] == 1:
            print(i + 1, end=" ")
    print("]")
