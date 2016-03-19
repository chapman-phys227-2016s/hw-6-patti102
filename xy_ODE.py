#! /usr/bin/env python

"""
File: xy_ODE.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates the solution to a differential equation by both numerical and symbolic
means and then plots a comparison of the various numerical means to a graph of the analytic
function of the solution given.

"""

import numpy as np
import matplotlib.pyplot as mp
import sympy as sp

def num_for_Eu(a, b, n, eps=1e-3):
    """Generates numerical solution array for the differential equation."""
    x = np.linspace(a, b, n+1)
    delta_x = (b - a) / float(n)
    I = np.zeros(n+1)
    I[0] = 1 + np.sqrt(eps)
    count = 0
    for i in range(n):
        I[count + 1] = I[count] + delta_x / float(2*(I[count] - 1))
        count = count + 1
    return x, I

def graph():
    """Plots numerical approximations of various accuracies of the differential equation
    and then plots the analytic function."""
    f = num_for_Eu(0, 4, 5)
    mp.plot(f[0], f[1], 'bo')
    f = num_for_Eu(0, 4, 17)
    mp.plot(f[0], f[1], 'ro')
    f = num_for_Eu(0, 4, 401)
    mp.plot(f[0], f[1], 'g-')
    mp.plot(f[0], 1 + np.sqrt(f[0] + 1), 'k-')
    mp.xlim([-0.01, 4.01])
    mp.title('Euler\'\s Forward Method and Analytic Function')
    mp.xlabel('x')
    mp.ylabel('Euler and Analytic Plots')
    
def symbolic_solver():
    """Solves the differential equation symbolically."""
    x = sp.symbols('x')
    f = sp.Function('f')
    print sp.dsolve(sp.Eq(sp.Derivative(f(x),x), 1 / (2 * (f(x) - 1))))[1]

def test_rightvalue():
    """Ensures that the numerical differential equation solver approaches the analytic
    value for the differential equation for high n values."""
    apt = np.fabs(num_for_Eu(0, 4, 1000)[1][-1] - 1 - np.sqrt(4 + 1e-3)) < 1e-3