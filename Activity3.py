# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:         Nathaniel Michaud, Luca Maddaleni, Landon Matak, Anthony Matl
# Group:        8
# Section:      273
# Assignment:   Lab 5
# Date:         25 September 2020

# Test 1: 2*x**3 + 3*x**2 + 4*x + 5, [-4, 10], x = -1.37
# Test 2: 2*x**3 + 3*x**2 + 4*x + 5, [5, 10], There are no zeros on this domain.
# Test 3: 8*x**3 + 0*x**2 + 3.7*x - 5.5, [0, 7], x = 0.711
# Test 4: 1.1*x**3 - 0.5*x**2 + 6*x - 4, [-8, 2], x = 0.651

from math import *
import numpy
import matplotlib.pyplot as plt

print('\nEnter the prompted information to find the root of A*x**3 + B*x**2 + C*x + D in the bound [a, b].')
print('Limitations: No roots tangent to the x-axis will be found and the domain must involve a single root.')

A = float(input('\nEnter the coefficient for A: '))
B = float(input('Enter the coefficient for B: '))
C = float(input('Enter the coefficient for C: '))
D = float(input('Enter the coefficient for D: '))
a1 = float(input('Enter the lower bound, a, for the domain: '))
b1 = float(input('Enter the upper bound, b, for the domain: '))

p = (a1+b1)/2 # This is the midpoint.
fa = A*a1**3 + B*a1**2 + C*a1 + D # The y value for x = a.
fp = A*p**3 + B*p**2 + C*p + D # The y value for x = p.
fb = A*b1**3 + B*b1**2 + C*b1 + D # The y value for x = b.
TOL = 0.000001
a = a1 # a1 is copied as a to keep the original domain for the graph.
b = b1 # b1 is copied as b to keep the original domain for the graph.

if fa*fb > 0 and fp != 0:
    print('\nFor the function', A, 'x^3 +', B, 'x^2 +', C, 'x +', D, ':')
    print('There are no zeros on this domain without consideration to tangent roots.')
elif fa == 0.0:
    print('\nFor the function', A, 'x^3 +', B, 'x^2 +', C, 'x +', D, ':')
    print('The root of the function is x =', a, '.')
elif fb == 0.0:
    print('\nFor the function', A, 'x^3 +', B, 'x^2 +', C, 'x +', D, ':')
    print('The root of the function is x =', b, '.')
elif fp == 0.0:
    print('\nFor the function', A, 'x^3 +', B, 'x^2 +', C, 'x +', D, ':')
    print('The root of the function is x =', p, '.')
else:
    while abs(b-a) > TOL:
        fa = A * a ** 3 + B * a ** 2 + C * a + D
        p = (a + b) / 2
        fp = A * p ** 3 + B * p ** 2 + C * p + D
        if fa*fp < 0:
            b = p
        else:
            a = p
    print('\nFor the function', A, 'x^3 +', B, 'x^2 +', C, 'x +', D, ':')
    print('The root of the function is x =', p, '.')

# The graph of the function is plotted on the user domain.
lower_range_val = a1
upper_range_val = b1
xvals = numpy.arange(lower_range_val, upper_range_val, 0.01)
yvals = A*(xvals)**3 + B*(xvals)**2 + C*(xvals) + D
plt.plot(xvals, yvals)
plt.show()