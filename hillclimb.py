import random

def objective_function(x, equation):
    return eval(equation)

def get_neighbors(x, step_size):
    return [x - step_size, x + step_size]

def hill_climbing(objective_function, equation, initial_solution, step_size, max_iter):
    current_solution = initial_solution
    current_value = objective_function(current_solution, equation)

    for _ in range(max_iter):
        neighbors = get_neighbors(current_solution, step_size)
        neighbor_values = [objective_function(neighbor, equation) for neighbor in neighbors]
        best_neighbor_value = max(neighbor_values) #for minimising, change to min() and change the if below to >=
        
        if best_neighbor_value <= current_value:
            break 
            
        best_neighbor_index = neighbor_values.index(best_neighbor_value)
        current_solution = neighbors[best_neighbor_index]
        current_value = best_neighbor_value

    return current_solution, current_value

if __name__ == "__main__":
    equation = input("Enter the equation (use 'x' as the variable): ")
    initial_solution = float(input("Enter the initial solution: "))
    step_size = float(input("Enter the step size: "))
    max_iter = int(input("Enter the maximum number of iterations: "))
    
    best_solution, best_value = hill_climbing(objective_function, equation, initial_solution, step_size, max_iter)
    print("Best solution found:", best_solution)
    print("Objective function value at best solution:", best_value)
