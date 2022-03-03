# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:19:14 2022

@author: miche
"""

import pulp
import sys


def option_a_equal_weights(n_variables):
    coe_arr= []
    for i in range(n_variables):
        coe_arr.append(1/n_variables)
    return coe_arr

def option_a_not_equal_weights(n_variables, alpha):
    coe_arr= []
    for i in range(n_variables):
        coe_arr.append(1/n_variables)
    return coe_arr


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


def parse_objectives(line,n,coe_arr):
    obj_deli = ';'
    coe_deli = ','
    objectives = line.strip().split(obj_deli)
    for index, objective in enumerate(objectives):
        objectives[index] = objective.split(',')
        objectives[index] = [coe_arr[index]*int(coefficent) for coefficent in objectives[index]]
    
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


def get_variables(n_variables):

    vars = []
    for i in range(n_variables):
        name = 'x' + str(i)
        vars.append(pulp.LpVariable(name,lowBound = 0) )

    return vars


def init_problem(variables, obj_fun_arr, constraints, n):
    # Conduct initial declaration of problem
    linear_problem = pulp.LpProblem("Maximizing_for_"+str(n)+"_objectives",pulp.LpMaximize)
    
    linear_expressions = []
    
    for j in range(n):
        linear_expressions.append(pulp.LpAffineExpression([(variables[i], obj_fun_arr[j][i]) for i in range(len(variables))]))
        
    lin_ex = pulp.LpAffineExpression(pulp.lpSum(linear_expressions))
  
    linear_problem += lin_ex
 
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
     
    lp = init_problem(variables, obj_fun_arr, constraints,  n_variables)
    solution=lp.solve()
   

   # solution = lp.solve()
        
        
    #first_lp = init_problem(variables, obj_fun_arr[0], constraints, 1)
    #solution = first_lp.solve()
    
    #print(type(lp.objective))
   
    
    print(str(pulp.LpStatus[solution])+" ; max value = "+str(pulp.value(lp.objective))+
      " ; x1_opt = "+str(pulp.value(variables[0]))+
      " ; x2_opt = "+str(pulp.value(variables[1])))
     #" ; x3_opt = "+str(pulp.value(variables[2])))
    
    

if __name__ == '__main__':
    main()