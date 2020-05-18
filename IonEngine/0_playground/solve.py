from sympy import * 
import sympy
x = Symbol('x')
B = Symbol('B')
A = Symbol('A')

sol = solve(x**3 + A*x**2 + 2*A**2*x -4*A**3 -B, x)
print(sol)
sol = sympy.simplify(sol)
print(sympy.latex(sol))