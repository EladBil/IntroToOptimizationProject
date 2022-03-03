# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:50:59 2022

@author: miche
"""
# import matplotlib.pyplot
import matplotlib.pyplot as plt 
import pulp

# import pandas and numpy for being able to store data in DataFrame format
import numpy as np
import pandas as pd

# define step-size
stepSize = 0.01

# initialize empty DataFrame for storing optimization outcomes
solutionTable = pd.DataFrame(columns=["alpha","x1_opt","x2_opt","obj_value"])

# iterate through alpha values from 0 to 1 with stepSize, and write PuLP solutions into solutionTable
# delcare optimization variables, using PuLP
x1 = pulp.LpVariable("x1",lowBound = 0)
x2 = pulp.LpVariable("x2",lowBound = 0)
for i in range(0,101,int(stepSize*100)):
        # declare the problem again
        linearProblem = pulp.LpProblem("Multi-objective linear maximization",pulp.LpMaximize)
        # add the objective function at sampled alpha
        linearProblem += (i/100)*(2*x1+3*x2)+(1-i/100)*(4*x1-2*x2)
        # add the constraints
        linearProblem += x1 + x2 <= 10
        linearProblem += 2*x1 + x2 <= 15
        # solve the problem 
        solution = linearProblem.solve()
        # write solutions into DataFrame
        solutionTable.loc[int(i/(stepSize*100))] = [i/100,
                                                     pulp.value(x1),
                                                     pulp.value(x2),
                                                     pulp.value(linearProblem.objective)]
print(str(pulp.LpStatus[solution])+" ; max value = "+str(pulp.value(linearProblem.objective))+
      " ; x1_opt = "+str(pulp.value(x1))+
      " ; x2_opt = "+str(pulp.value(x2)))

# visualize optimization outcome, using matplotlib.pyplot
# -- set figure size
plt.figure(figsize=(20,10))
# -- create line plot
plt.plot(solutionTable["alpha"],solutionTable["obj_value"],color="red")
# -- add axis labels
plt.xlabel("alpha",size=20)
plt.ylabel("obj_value",size=20)
# -- add plot title
plt.title("Optimal combined objective function value as a function of alpha",size=32)
# -- show plot
plt.show()
