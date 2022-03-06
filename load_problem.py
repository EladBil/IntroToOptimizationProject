def parse_objectives(line,n,coe_arr):
    obj_deli = ';'
    objectives = line.strip().split(obj_deli)
    for index, objective in enumerate(objectives):
        objectives[index] = objective.split(',')
        objectives[index] = [coe_arr[index]*int(coefficent) for coefficent in objectives[index]]
    
    return objectives


def parse_constraints(line):

    obj_deli = ';'
    coe_deli = ','
    objectives = line.strip().split(obj_deli)
    
    for index, objective in enumerate(objectives):
        objectives[index] = objective.split(coe_deli)
        objectives[index] = [int(coefficent) for coefficent in objectives[index]]
        objectives[index] = (objectives[index][:-1], objectives[index][-1])
    return objectives


def get_problem_data(file_path):
    try:
        file = open(file_path, "+r")
        num_of_variables = int(file.readline())
        coe_arr = option_a_equal_weights(num_of_variables)
        objectives_functions_arr = parse_objectives(file.readline(),num_of_variables,coe_arr)
        constraints = parse_constraints(file.readline())

        
        print(num_of_variables)
        print(objectives_functions_arr)
        print(constraints)

        return num_of_variables, objectives_functions_arr, constraints

    except:
        print("File not found!!!")
