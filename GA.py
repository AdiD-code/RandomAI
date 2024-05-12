import random

def fitness_function(x): 
    return x**2 

def create_population(population_size, min_value, max_value): 
    return [random.uniform(min_value, max_value) for _ in range(population_size)] 

def tournament_selection(population, fitness_values, tournament_size): 
    selected = [] 
    for _ in range(len(population)): 
        tournament = random.sample(list(enumerate(population)), tournament_size) 
        tournament_fitness = [(idx, fitness_values[idx]) for idx, _ in tournament] 
        winner = max(tournament_fitness, key=lambda x: x[1]) 
        selected.append(population[winner[0]])

    return selected

def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        child1 = parent1
        child2 = parent2

        crossover_point = random.uniform(0, 1)
        child1 = crossover_point * parent1 + (1 - crossover_point) * parent2
        child2 = crossover_point * parent2 + (1 - crossover_point) * parent1

        return child1, child2
    
    return parent1, parent2

def mutate(individual, mutation_rate, min_value, max_value):
    if random.random() < mutation_rate:
        mutated_value = random.uniform(min_value, max_value)

        return mutated_value
    
    return individual

def genetic_algorithm(population_size, min_value, max_value, generations, tournament_size, crossover_rate, mutation_rate): 
    population = create_population(population_size, min_value, max_value) 
    for gen in range(generations): 
        fitness_values = [fitness_function(x) for x in population] 
        new_population = [] 
        
        best_index = fitness_values.index(max(fitness_values)) 
        best_individual = population[best_index]
        best_fitness = fitness_values[best_index]
        
        print(f"Generation {gen + 1}: Best individual = {best_individual}, Best fitness = {best_fitness}")
        
        new_population.append(best_individual) 
        
        selected_parents = tournament_selection(population, fitness_values, tournament_size) 

        for i in range(0, len(selected_parents), 2): 
            parent1 = selected_parents[i] 
            parent2 = selected_parents[i + 1] 
            child1, child2 = crossover(parent1, parent2, crossover_rate)

            child1 = mutate(child1, mutation_rate, min_value, max_value) 
            child2 = mutate(child2, mutation_rate, min_value, max_value) 
            new_population.extend([child1, child2]) 
        population = new_population[:population_size] 
        
    best_index = fitness_values.index(max(fitness_values)) 
    best_individual = population[best_index] 
    best_fitness = fitness_function(best_individual)

    return best_individual, best_fitness 

# Predefined parameters
population_size = 100 
min_value = -10 
max_value = 10 
generations = 10  # Reduced for demonstration
tournament_size = 3 
crossover_rate = 0.8 
mutation_rate = 0.01 

# Uncomment the below section to take parameters by user input
"""
population_size = int(input("Enter population size: "))
min_value = float(input("Enter minimum value: "))
max_value = float(input("Enter maximum value: "))
generations = int(input("Enter number of generations: "))
tournament_size = int(input("Enter tournament size: "))
crossover_rate = float(input("Enter crossover rate: "))
mutation_rate = float(input("Enter mutation rate: "))
"""

best_individual, best_fitness = genetic_algorithm(population_size, min_value, max_value, generations, tournament_size, crossover_rate, mutation_rate) 
print("Final Best individual:", best_individual) 
print("Final Best fitness:", best_fitness)


