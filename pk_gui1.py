
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
    rhs_expr = eval(parser.expr(rhs_string).compile())
    rhs_expr = expand(rhs_expr)    
    
    # Append variables and expressions to list
    var_list.append(var)
    expr_list.append(rhs_expr)
    
    return (var_list, expr_list)


# --- Main code block ---
# Call function diff_eqs()
varList, exprList = diff_eqs()



