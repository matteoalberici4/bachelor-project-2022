#!/usr/bin/env python3

# Bachelor Project 2022
# Matteo Alberici

from z3.z3 import *

# Int: creates an Int variable
x = Int('x')
y = Int('y')
print()
print('1. Int Variables')
print(x, y)

print()

# solve: solves a system of constraints
print('2. Solve')
print('x > 2, y < 10, x + 2*y == 7')
solve(x > 2, y < 10, x + 2 * y == 7)

print()

# Question: what if I remove the first two constraints?

# simplify: simplifies a given formula
z = simplify(x + y + 2 * x + 3)
print('3. Simplify')
print('x + y + 2*x + 3  -> ', z)

print()

# Question:
# print x**2 + y**2 >= 1
# set_option(html_mode=False)
# print x**2 + y**2 >= 1

# Traversing Expressions
print('4. Traversing Expressions')
n = x + y >= 3
print('n:', n)
print("num_args:", n.num_args())
print("children:", n.children())
print("1st child:", n.arg(0))
print("operator:", n.decl())

print()

# Nonlinear Polynomial Constraints
print('5. Nonlinear Polynomial Constraints')
x = Real('x')
y = Real('y')
print('Real variables:', x, y)
print('Solve: x**2 + y**2 > 3, x**3 + y < 5')
solve(x ** 2 + y ** 2 > 3, x ** 3 + y < 5)

# set_option: configures the Z3 environment
print('6. Set Options')
print("Let's set a precision of 30")
set_option(precision=30)
print('Solve: x**2 + y**2 == 3, x**3 == 2')
solve(x ** 2 + y ** 2 == 3, x ** 3 == 2)
# Remark: '?' indicates the output is truncated

# Q: creates a rational number given a numerator and a denominator
print('7. Q Function')
z = Q(1, 3)
print('Q(1/3) =', z)

print()

# Unsatisfiable systems
print('8. Unsatisfiable Systems')
print('Solve: x > 4, x < 0')
solve(x > 4, x < 0)

print()

# Displaying rational numbers in decimal notation
print('9. Rational Numbers in Decimal Notation')
print('Solve: 3*x == 1')
solve(3*x == 1)
print("Let's set to True the option 'rational_to_decimal'")
set_option(rational_to_decimal=True)
print('Solve: 3*x == 1')
solve(3*x == 1)

print()

# Boolean Logic
print('10. Boolean Logic')
p = Bool('p')
q = Bool('q')
print('Bool Variables:', p, q)
print('Solve: And(p, q, True)')
solve(And(p, q, True))
print('Solve: Implies(p, q), p == Not(q), Or(Not(p, q))')
solve(Implies(p, q), p == Not(q), Or(Not(p, q)))
