import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify, expand


class Derivatives:

    def __init__(self, name, age):
        pass
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


    ''' 

    Take all orders of derivative and evaluate using x_val, returns an 
    array of all derivative that have been evaluated

    '''
    def f_of_x(coef, exp, x_val):
        val = []
        for i in range(max(exp)):
            eval = 0
            new_term = Derivatives.derive_power(coef, exp)
            coef = new_term[0]
            exp = new_term[1]
            for i in range(len(coef)):
                if (exp[i] < 0):
                    continue
                eval = eval + coef[i]*(x_val**exp[i]);
            val.append(eval)
        return val

    ''' 

    Take a single function and evaluate using x_val, returns 
    the evaluated function (int)

    '''
    def evaluate_single(coef, exp, x_val):
        eval = 0
        for i in range(len(coef)):
            if (exp[i] < 0):
                continue
            if (exp[i] == 0):
                eval = eval + coef[i]
                continue
            eval = eval + coef[i]*(x_val**exp[i]);
        return eval
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
            new_term = Derivatives.derive_power(coef, exp)
            coef = new_term[0]
            exp = new_term[1]
            v = [coef, exp]
            val.append(v)
        return val
    
class NumericalAnalysis:

    def __init__(self, name, age):
        pass
    def get_binomial_expansion(expr):
        x = symbols('x')
        return expand(expr)
    
    def bisection_method(coef, exp, _a, _b, limit = 0, show_each_iteration = False):
        c = 0
        a = _a
        b = _b
        q = 0
        eval = 0
        #if (limit > 0):
        #c = (a + b)/2
        for i in range(limit):
            c = (a + b)/2
            q = Derivatives.evaluate_single(coef, exp, c)
            if (q < 0):
                a = c
            elif (q > 0):
                b = c
            if (show_each_iteration):
                print("Iteration: " + str(i) + " = " + str(q))
                

    def get_taylor_series_as_text(orig_f_coe, orig_f_exp, x0, fofx0):
        factorial = 1
        multiplier = 1
        eq = 0
        text = ""
        text = str(Derivatives.evaluate_single(orig_f_coe, orig_f_exp, x0)) + " + "
        for i in range(len(fofx0)):
            x = (x0 * -1)
            eq = (fofx0[i]/factorial)
            z = ""
            if (x-1 == 0):
                z = "(" + "x+" + str(x) + ")**" + str(i+1)
            else:
                z = "(" + "x" + str(x) + ")**" + str(i+1)
            if (eq==1):
                text = text + z
            else:
                text = text + str(eq) + "*" + z
            if (i < len(fofx0)-1):
                text = text + " + "
            multiplier = multiplier + 1
            factorial = factorial * multiplier
        return text
    
    def get_taylor_series_as_graph(orig_f_coe, orig_f_exp, x0, fofx0):
        factorial = 1
        multiplier = 1
        eq = 0
        expr = ""
        expr = str(Derivatives.evaluate_single(orig_f_coe, orig_f_exp, x0)) + " + "
        for i in range(len(fofx0)):
            x = (x0 * -1)
            eq = (fofx0[i]/factorial)
            z = ""
            if (x-1 == 0):
                z = "(" + "x+" + str(x) + ")**" + str(i+1)
            else:
                z = "(" + "x" + str(x) + ")**" + str(i+1)
            if (eq==1):
                expr = expr + z
            else:
                expr = expr + str(eq) + "*" + z
            if (i < len(fofx0)-1):
                expr = expr + " + "
            multiplier = multiplier + 1
            factorial = factorial * multiplier
            
        # Define symbols
        x = symbols('x')
        parse = sympify(expr)
        
        # 4. Convert symbolic → numerical function
        f = lambdify(x, parse, 'numpy')

        # 5. Generate x values
        x_vals = np.linspace(-5, 5, 400)

        # 6. Compute y values
        y_vals = f(x_vals)

        # 7. Plot
        plt.plot(x_vals, y_vals)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("f(x) = " + str(expr), fontsize=5)
        plt.grid()

        plt.show()
