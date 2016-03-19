#! /usr/bin/env python

"""
File: xy_ODE.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates the solution to a differential equation by both numerical and symbolic
means and then generates a table illustrating the oscillatory nature of its solutions within
a certain delta t interval and the interval on which this oscillation is both decreasing
and increasing in its overall magnitude for the solution.

"""

import numpy as np
import matplotlib.pyplot as mp
import sympy as sp
import math as math

def num_for_Eu(n, I_0):
    """Generates numerical solution array for the differential equation."""
    delta_t = 11 / float(n)
    I = np.zeros(n+1)
    count = 0
    for i in range(n):
        I[count] = I_0 * (1 - delta_t)**count
        count = count + 1
    return delta_t, I

def tabler():
    """Generates a table comparing the first 4 values of various delta t values."""
    print
    print '%15s' % ('Oscillation Demonstration First 4 Values')
    print
    print '%10s %10s %10s %10s %10s' % ('Delta t', 'Value 1', 'Value 2', 'Value 3', 'Value 4')
    print
    f = num_for_Eu(9, 1)
    print '%10.2f %10f %10f %10f %10f' % (f[0], f[1][0], f[1][1], f[1][2], f[1][3])
    f = num_for_Eu(7, 1)
    print '%10.2f %10f %10f %10f %10f' % (f[0], f[1][0], f[1][1], f[1][2], f[1][3])
    f = num_for_Eu(6, 1)
    print '%10.2f %10f %10f %10f %10f' % (f[0], f[1][0], f[1][1], f[1][2], f[1][3])
    f = num_for_Eu(4, 1)
    print '%10.2f %10f %10f %10f %10f' % (f[0], f[1][0], f[1][1], f[1][2], f[1][3])
    print
    
def symbolic_solver():
    """Solves the differential equation symbolically."""
    x = sp.symbols('x')
    f = sp.Function('f')
    print sp.dsolve(sp.Eq(sp.Derivative(f(x),x), - f(x)))
    
def test_rightvalue():
    """Ensures that the numerical differential equation solver approaches the analytic
    value for the differential equation."""
    apt = np.fabs(num_for_Eu(9, 1)[1][-1] - 1 - np.exp(-10)) < 1e-3


