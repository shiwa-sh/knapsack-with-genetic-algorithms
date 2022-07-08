import random
from sklearn import preprocessing
global total_weight, val, w  # global variables
total_weight = 0
val = []
w = []


def initial_chromosome_generation(population_size, chromosome_size):
    first_generation = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_size):

            chromosome.append(random.randint(0, 1))

        first_generation.append(chromosome)

    return first_generation


def fitness_function(population, population_size, chromosome_size):
    current_total_weight = 0
    fitness = []
    current_fitness = 0
    for i in range(population_size):
        for k in range(chromosome_size):
            if population[i][k] == 1:
                current_fitness += val[k]
                current_total_weight += w[k]

        if current_total_weight <= total_weight:
            fitness.append(current_fitness)
        else:
            fitness.append(0)

    return fitness


def selection(population):
    population_fitness = fitness_function(population, len(population), len(population[0]))
    ''' Roulette selection '''
    total_fitness = sum(population_fitness)
    select_probability = []
    # for i in range(len(population)):
    #     select_probability.append(population_fitness[i] / total_fitness)

    probability = []
    previous_probability = 0
    for i in range(len(select_probability)):
        probability.append(select_probability[i] + previous_probability)

    normalized_probability = preprocessing.normalize(probability, norm='l1')
    selected_population = []
    current_fitness_sum = 0
    for j in range(2):
        bound = random.uniform(0, max(probability))
        for k in range (len(population[0])):
            current_fitness_sum = current_fitness_sum + normalized_probability[k]
            if current_fitness_sum >= bound:
                selected_population.append(population[k])
                break

def crossover(first_chromosome, second_chromosome):

    crossover_limit = random.randint(1, len(first_chromosome)-1)
    crossed_chromosome = []
    new_chromosome = []
    new_chromosome = first_chromosome[:crossover_limit] + second_chromosome[crossover_limit:]
    crossed_chromosome.append(new_chromosome)
    new_chromosome = second_chromosome[:crossover_limit] + first_chromosome[crossover_limit:]
    crossed_chromosome.append(new_chromosome)

    # for i in range(len(population)):
    #     if random.random() < crossover_rate:
    #         for j in range(len(population[i])):
    #             if random.random() < 0.5:
    #                 population[i][j] = 1 if population[i][j] == 0 else 0

    return crossed_chromosome


def mutation(chromosome):

    for i in range(len(chromosome)):
        mutation_rate = random.uniform(0,1)
        if mutation_rate < 0.5:
            chromosome[i] = 1 if chromosome[i] == 0 else 0
    return chromosome


def main():
    # population_max_size = 100
    population_size = 10
    chromosome_size = 10
    mutation_rate = 0.1
    crossover_rate = 0.5
    generation_number = 0
    population = initial_chromosome_generation(population_size, chromosome_size)
    fitness_values = []
    for i in range(len(population)):
        fitness_values.append(fitness_function(population[i]))

    while True:
        generation_number += 1
        print("Generation number: ", generation_number)
        print("Population: ", population)
        print("Fitness values: ", fitness_values)
        selected_population = selection(population, fitness_values)
        print("Selected population: ", selected_population)
         mutated_population = mutation(selected_population, mutation_rate)
        print("Mutated population: ", mutated_population)
        crossed_population = crossover(mutated_population, crossover_rate)
        print("Crossed population: ", crossed_population)
        fitness_values = []
        for i in range(len(crossed_population)):
            fitness_values.append(fitness_function(crossed_population[i]))
        population = crossed_population
        print("Fitness values: ", fitness_values)
        if fitness_values[0] == chromosome_size:
            print("Solution found in generation number: ", generation_number)
            print("Solution: ", population[0])
                # break



