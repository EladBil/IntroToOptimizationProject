import pulp


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


def get_variables(n_variables):

    vars = []
    for i in range(n_variables):
        name = 'x' + str(i)
        vars.append(pulp.LpVariable(name,lowBound = 0) )

    return vars
