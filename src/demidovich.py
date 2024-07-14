from typing import Any
from sympy import Eq, Interval,  Symbol, atan, ceiling, cos, diff, floor,  integrate, limit, log, minimum, oo, root, sin, solve, summation, symbols, tan
import numpy as np
import matplotlib.pyplot as plt
from os import mkdir

# 99, 100, 253, 279 g, 299, 555-559, 1203, 1656-1658, 1807-1810, 3022, 3023

x = symbols('x', real=True)
n: Any = Symbol('n', positive=True, integer=True)
a, b, c = symbols('a b c', positive=True)


def solve_99():
    f = n**2 - 9*n - 100
    min_val = minimum(f, n, Interval(1, oo, right_open=True))
    g = x**2 - 9*x - 100 - min_val
    n_min = solve(g, x)[0]
    
    if abs(n_min - round(n_min)) >= 0.0000001:
        result = min(f.subs({n: floor(n_min)}), f.subs({n: ceiling(n_min)}))
    else :
        result = n_min
    
    print(f"\n99: minimum value of sequence x_n = n^2 - 9*n - 100 is x = {result}")
    return result


def solve_100():
    f = n + 100/n
    min_val = minimum(f, n, Interval(1, oo, right_open=True))
    g = x + 100/x - min_val
    n_min = solve(g, x)[0]
    
    if abs(n_min - round(n_min)) >= 0.0000001:
        result = min(f.subs({n: floor(n_min)}), f.subs({n: ceiling(n_min)}))
    else :
        result = min_val
    
    print(f"\n100: minimum value of sequence x_n = n + 100/n is x = {result}")
    return result

def solve_253():
    x = np.arange(-5, 5, 0.01)
    y = (lambda x: x + 1/x)(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$y = x + \frac{1}{x}$', color='b')

    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(r'$y = x + \frac{1}{x}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-100, 100)
    plt.legend(loc='upper right')

    try:
        mkdir('graphs')
    except FileExistsError:
        pass
    plt.savefig('graphs/graph_253.png')
    print("\n253: Saved graph of 253 into ./graphs/graph_253.png\n")


def solve_279():
    x = np.arange(-5, 5, 0.01)
    y = np.exp(1/x**2)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$y = e^(\frac{1}{x^2})$', color='b')

    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(r'$y = e^(\frac{1}{x^2})$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(0, 100)
    plt.legend(loc='upper right')

    try:
        mkdir('graphs')
    except FileExistsError:
        pass
    plt.savefig('graphs/graph_279.png')
    print("\n279: Saved graph into ./graphs/graph_279.png\n")


def solve_299():
    x = np.arange(-5, 5, 0.001)
    y = np.sin(1/x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$y = \sin(\frac{1}{x})$', color='b')

    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(r'$y = \sin(\frac{1}{x})$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')

    try:
        mkdir('graphs')
    except FileExistsError:
        pass
    plt.savefig('graphs/graph_299.png')
    print("\n299: Saved graph into ./graphs/graph_299.png\n")


def solve_555():
    term = ((root(a, n) + root(b, n))/2)**n # type: ignore
    result = limit(term, n, oo).doit()
    print(f"\n555: limit of {term} is {result}\n")
    return result


def solve_556():
    term = ((a**x + b**x + c**x)/3)**(1/x)
    result = limit(term, x, 0).doit()
    print(f"\n556: limit of {term} is {result}\n")
    return result


def solve_557():
    term = ((a**(x+1) + b**(x+1) + c**(x+1))/(a+b+c))**(1/x)
    result = limit(term, x, 0).doit()
    print(f"\n557: limit of {term} is {result}\n")
    return result


def solve_558():
    term = ((a**(x**2) + b**(x**2))/(a**x + b**x))**(1/x)
    result = limit(term, x, 0).doit()
    print(f"\n558: limit of {term} is {result}\n")
    return result


def solve_559():
    term = (a**(x**2) - b**(x**2))/(a**x - b**x)**2
    result = limit(term, x, a).doit()
    print(f"\n559: limit of {term} is {result}\n")
    return result


def solve_1203():
    f = x**2 * sin(a * x)
    result = diff(f, (x, n))
    print(f"\n1203: nth derivative of {f} is {result}\n")
    return result


def solve_1656():
    f = (2 * x - 3) ** 10
    result = integrate(f)
    print(f"\n1656: integral of {f} is {result} \n")
    return result


def solve_1657():
    f = root(1 - 3*x, 3)
    result = integrate(f)
    print(f"\n1657: integral of {f} is {result}\n")
    return result


def solve_1658():
    f = 1 / root(2 - 5*x, 2) #type: ignore
    result = integrate(f)
    print(f"\n1658: integral of {f} is {result}\n")
    return result


def solve_1807():
    f = log(x + root(1 + x**2, 2))
    result = integrate(f)
    print(f"\n1807: integral of {f} is {result}\n")
    return result


def solve_1808():
    f = x * log((1 + x) / (1 - x))
    result = integrate(f)
    print(f"\n1808: integral of {f} is {result}\n")
    return result


def solve_1809():
    f = atan(root(x, 2))
    result = integrate(f)
    print(f"\n1809: integral of {f} is {result}\n")
    return result


def solve_1810():
    f = sin(x) * log(tan(x)) # type: ignore
    result = integrate(f)
    print(f"\n1810: integral of {f} is {result}\n")
    return result


def solve_3022():
    f = sin(2*n - 1)*x/(2*n - 1)
    s = summation(f, (n, 1, oo)).doit() # type: ignore
    print(f"\n3022: sum of {f} is {s} \n {s.subs(x, 1).doit()}\n") # type: ignore
    return s


def solve_3023():
    f = ((-1)**n) * (cos(n*x)/(n**2 - 1))
    s = summation(f, (n, 2, oo)).doit() # type: ignore 
    print(f"\n3023: sum of {f} is {s} \n {s.subs(x, 1).doit()}\n") # type: ignore
    return s


def run_demidovich() -> None:
    solve_99()
    solve_100()
    solve_253()
    solve_279()
    solve_299()
    solve_555()
    solve_556()
    solve_557()
    solve_558()
    solve_559()
    solve_1203()
    solve_1656()
    solve_1657()
    solve_1658()
    solve_1807()
    solve_1808()
    solve_1809()
    solve_1810()
    solve_3022()
    solve_3023()


if __name__ == "__main__":
    run_demidovich()
