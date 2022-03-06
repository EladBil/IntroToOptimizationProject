# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:19:14 2022

@author: miche
"""

import pulp
import sys


def parse_constraints(line):

    obj_deli = ';'
    coe_deli = ','
    objectives = line.strip().split(obj_deli)
    
    for index, objective in enumerate(objectives):
        objectives[index] = objective.split(coe_deli)
        objectives[index] = [int(coefficent) for coefficent in objectives[index]]
        objectives[index] = (objectives[index][:-1], objectives[index][-1])
    return objectives

def add_constraint(variables, obj_fun):
    
    return


def parse_objectives(line):

    obj_deli = ';'
    objectives = line.strip().split(obj_deli)
    
    for index, objective in enumerate(objectives):
        objectives[index] = objective.split(',')
        objectives[index] = [int(coefficent) for coefficent in objectives[index]]
    
    return objectives


def get_problem_data(file_path):
    try:
        file = open(file_path, "+r")
        num_of_variables = int(file.readline())
        objectives_functions_arr = parse_objectives(file.readline())
        constraints = parse_constraints(file.readline())

        
        # print(num_of_variables)
        # print(objectives_functions_arr)
        # print(constraints)

        return num_of_variables, objectives_functions_arr, constraints

    except:
        print("File not found!!!")


def get_variables(n_variables):

    vars = []
    for i in range(n_variables):
        name = 'x' + str(i)
        vars.append(pulp.LpVariable(name,lowBound = 0) )

    return vars


def init_problem(variables, obj_fun_arr, constraints, i):
    # Conduct initial declaration of problem
    linear_problem = pulp.LpProblem("Maximizing_for_"+str(i)+"_objective",pulp.LpMaximize)

    linear_problem += pulp.LpAffineExpression(
        [(variables[i], obj_fun_arr[i]) for i in range(len(variables))])
    
    # print(linear_problem.objective)
    
    for index, constraint in enumerate(constraints):
        expression = pulp.LpAffineExpression(
        [(variables[i], constraint[0][i]) for i in range(len(variables))])
        linear_problem+=pulp.LpConstraint(
            expression,
            -1,
           index + 1,
           int(constraint[1]))

    

    return linear_problem


def main():
    file_path = sys.argv[1]
    n_variables, obj_fun_arr, constraints = get_problem_data(file_path)
    variables = get_variables(n_variables)
    print(variables)
    new_constraints =[]
    for i in range(len(obj_fun_arr)): 
        lp = init_problem(variables, obj_fun_arr[i], constraints, i)
        solution=lp.solve()
        new_constraints.append(pulp.LpConstraint(lp.objective,-1,100+i,pulp.value(lp.objective)))
        for j in new_constraints:
            lp+=j
        solution = lp.solve()
        
        
    #first_lp = init_problem(variables, obj_fun_arr[0], constraints, 1)
    #solution = first_lp.solve()
    
    print(type(lp.objective))
   
    
    print(str(pulp.LpStatus[solution])+" ; max value = "+str(pulp.value(lp.objective))+
      " ; x1_opt = "+str(pulp.value(variables[0]))+
      " ; x2_opt = "+str(pulp.value(variables[1])))
     #" ; x3_opt = "+str(pulp.value(variables[2])))
    
    

if __name__ == '__main__':
    main()