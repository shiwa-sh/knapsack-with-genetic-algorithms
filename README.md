# kanpsack problem with gentic algorithm

The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible
## genetic algorithm
### chromosome structure
chromosome structure: an array of binary values 
    with length of item count
    1 means that item is selected
    0 means that item is not selected
 ### population initialization
 if number of items are less than 7 population size will be 2^N otherwite it will be 100
 ### selection
 Roulette Wheel Selection (RWS)
    a set of N elements, each with a fitness F0 ... Fn, it finds the sum
    of the fitness for each element in the set and gives each element a chance to be selected with the
    individual fitness over the sum of the fitness.
