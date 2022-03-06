import scalarization_method
import small_epsilon_method
import load_problem
import sys
import pulp
import matplotlib


def get_weight_performance_graphs(file_path, n_variables):


    weigths = []
    solutions_value = []
    for i in range(100):
        coe_arr = scalarization_method.random_weights(n_variables)
        weigths.append(coe_arr)
        sm_n_variables, sm_obj_fun_arr, sm_constraints = scalarization_method.get_problem_data(file_path, coe_arr)
        sm_variables = load_problem.get_variables(sm_n_variables)
        sm_linear_problem = scalarization_method.init_problem(sm_variables, sm_obj_fun_arr, sm_constraints, sm_n_variables)
        sm_solution = sm_linear_problem.solve()
        solutions_value.append(pulp.value(sm_linear_problem.objective))
        
    original_stdout = sys.stdout # Save a reference to the original standard output

    with open('weight_results.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        for weigth, value in zip(weigths, solutions_value):
            print(*weigth,str(value), sep=",")
        sys.stdout = original_stdout # Reset the standard output to its original value
    
    



def main():
    file_path = sys.argv[1]
    
    se_n_variables, se_obj_fun_arr, se_constraints = small_epsilon_method.get_problem_data(file_path)
    sm_n_variables, sm_obj_fun_arr, sm_constraints = scalarization_method.get_problem_data(file_path)
    get_weight_performance_graphs(file_path, sm_n_variables)

    # se_variables = load_problem.get_variables(se_n_variables)
    # sm_variables = load_problem.get_variables(sm_n_variables)


    # se_linear_problem = (se_variables, se_obj_fun_arr, se_constraints,  se_n_variables)
    # sm_linear_problem = scalarization_method.init_problem(sm_variables, sm_obj_fun_arr, sm_constraints, sm_n_variables)
    
    # new_constraints =[]
    # for i in range(len(se_obj_fun_arr)): 
    #     se_linear_problem = small_epsilon_method.init_problem(se_variables, se_obj_fun_arr[i], se_constraints, i)
    #     se_solution = se_linear_problem.solve()
    #     new_constraints.append(pulp.LpConstraint(
    #         se_linear_problem.objective,
    #         -1,
    #         100+i,
    #         pulp.value(se_linear_problem.objective
    #         )))
    #     for j in new_constraints:
    #         se_linear_problem += j
    #     se_solution = se_linear_problem.solve()

    # sm_solution = sm_linear_problem.solve()


    # print("Small Epsilon Method:")
    # print(str(pulp.LpStatus[se_solution])+" ; max value = "+str(pulp.value(se_linear_problem.objective))+
    #   " ; x1_opt = "+str(pulp.value(se_variables[0]))+
    #   " ; x2_opt = "+str(pulp.value(se_variables[1])))

    # print("Scalarization Method:")
    # print(str(pulp.LpStatus[sm_solution])+" ; max value = "+str(pulp.value(sm_linear_problem.objective))+
    #   " ; x1_opt = "+str(pulp.value(sm_variables[0]))+
    #   " ; x2_opt = "+str(pulp.value(sm_variables[1])))
    


if __name__ == '__main__':
    main()