
"""
PkPy:
Package to develop a first order ODE Solver and Visualizer for PK in Python

Version1: Just solve one equation typed in interactively by user.
No GUI yet!

Author: Sudin Bhattacharya
7/28/16

"""

from sympy import *
from math import *
import parser
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Function to enter and parse diff. eq.
def diff_eqs():
    """Reads in equation from user and returns variables and RHS expressions"""
    var_list = []
    expr_list = []
    
    eq_string = input("Type in the diff. eq. in the form x' = f(x): ")
    
    # Parse the equation string
    var_string = eq_string.split("=")[0].split("'")[0].strip()
    rhs_string = eq_string.split("=")[1].strip()
    
    # Assign variable symbol to variable name to process with sympy
    var = symbols(var_string)
    exec(var_string + " = symbols('" + var_string + "')") 

    # Evaluate RHS of entered diff. eq.
    rhs_expr = sympify(rhs_string)
    rhs_expr = expand(rhs_expr)    
    
    # Append variables and expressions to list
    var_list.append(var)
    expr_list.append(rhs_expr)
    
    return (var_list, expr_list)


# Function to enter initial condition
def init_conds():
    """Reads in and returns initial conditions for variables"""
    ic_list = []
    ic_string = input("Enter initial value of variable: ")
    ic_val = float(ic_string)
    ic_list.append(ic_val)
    return ic_list 


# Function to enter stop time and time increment
def time_params():
    """Reads in and returns stop time and time increment"""
    stop_time = float(input("Enter stop time: "))
    time_inc = float(input("Enter time increment: "))
    return (stop_time, time_inc)


# Function to return derivatives
def f_derivs(varList, varVals, exprList, t):
    """Returns derivatives evaluated at time t"""
    derivVals = []
    numVars = len(varVals)
    for i in range(numVars):
        derivVal = exprList[i].subs(varList[i], varVals[i])
        derivVals.append(derivVal)
        
    return derivVals
        
    
    

# --- Main code block ---
# Call function diff_eqs()
varList, exprList = diff_eqs()

# Call function init_conds()
icList = init_conds()

# Call function time_params()
stopTime, timeInc = time_params()

# Set up time array for ODE solver
t = np.arange(0., stopTime, timeInc)

# Bundle parameters for ODE solver
params = []
