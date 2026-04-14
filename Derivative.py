import numpy as np
import math
import matplotlib.pyplot as plt

'''
example: 

Note: Please simplify the equation until it satisfies this format, Cx^n + Cx^n+1 + Cx^n+2 ... where C is any constant, x is the variable and n is the exponent
Note: This might not work with negative exponents when passing in an expression, so make sure that all exponents are positive.

2x^3 + 3x -8
coeficient = [2, 3, -8]
exponents = [3, 1, 0]

'''
# Single Derivative
def derive_power(coeficients, exponents):
    ret_term = []
    ret_exp = []
    for i in range(len(coeficients)):
        ret_term.append(coeficients[i] * exponents[i])
        ret_exp.append(exponents[i] - 1)
    return [ret_term, ret_exp]
    

''' Take all orders of derivative and evaluate using x_val, returns an array of all derivative that have been evaluated'''
def f_of_x(coef, exp, x_val):
    val = []
    for i in range(max(exp)):
        eval = 0
        new_term = derive_power(coef, exp)
        coef = new_term[0]
        exp = new_term[1]
        for i in range(len(coef)):
            if (exp[i] < 0):
                continue
            eval = eval + coef[i]*(x_val**exp[i]);
        val.append(eval)
    return val

''' 
Returns an array of all orders of derivative
[ [][], [][], [][]] - the returned array will have two arrays in one element
the first array element is th coeficient and the second is the exponents in respective order
example:
2x^3 +3x -1
[[6, 3, 0] [3, 1, 0], [18, 3, 0] [2, 0, -1], [36, 1, 0] [1, -1, -2]]
'''
def get_all_derivative(coef, exp):
    val= []
    for i in range(len(coef)):
        new_term = derive_power(coef, exp)
        coef = new_term[0]
        exp = new_term[1]
        v = [coef, exp]
        val.append(v)
    return val
