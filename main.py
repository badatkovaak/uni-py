from sympy import symbols, exp
# from sympy.core.symbol import symbols
from sympy.functions.combinatorial.factorials import factorial
from sympy.solvers.inequalities import reduce_inequalities

n = symbols('n', integer=True, positive=True)
f = factorial(n)
left = (n / exp(1)) ** n
right = exp(1) * (n / 2) ** n
# ineq1 = reduce_inequalities(left < f)
ineq2 = reduce_inequalities(f < right)
# print(ineq1)
print(ineq2)
