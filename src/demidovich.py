# import sympy as sp
from sympy import Symbol, atan, cos, diff, exp, integrate, limit, log, oo, root, simplify, sin, summation, symbols, tan
from sympy.plotting.plot import plot
import numpy as np
import matplotlib.pyplot as plt

# 99, 100, 253, 279 g, 299, 555-559, 1203, 1656-1658, 1807-1810, 3022, 3023

x = symbols('x', real=True)
n = Symbol('n', positive=True, integer=True)
a, b, c = symbols('a b c', positive=True)


def solve_99():
    # f = n**2 - 9*n - 100
    pass


def solve_100():
    # f = n + 100/n
    pass


def solve_253():
    f = x + 1/x
    plot(f, (x, -2, 2), ylim=(-20, 20))


def solve_279():
    # f = exp(1/x**2)
    # plot(f, (x, -3, 3), ylim=(-20, 100))
    x = np.linspace(-5, 5, 4000)
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

    plt.show()


def solve_299():
    x = np.linspace(-5, 5, 4000)
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

    plt.show()


def solve_555():
    term = ((root(a, n) + root(b, n))/2)**n
    result = limit(term, n, oo).doit()
    print(f"555: limit of {term} is {result}\n")
    return result


def solve_556():
    term = ((a**x + b**x + c**x)/3)**(1/x)
    result = limit(term, x, 0).doit()
    print(f"556: limit of {term} is {result}\n")
    return result


def solve_557():
    term = ((a**(x+1) + b**(x+1) + c**(x+1))/(a+b+c))**(1/x)
    result = limit(term, x, 0).doit()
    print(f"557: limit of {term} is {result}\n")
    return result


def solve_558():
    term = ((a**(x**2) + b**(x**2))/(a**x + b**x))**(1/x)
    result = limit(term, x, 0).doit()
    print(f"558: limit of {term} is {result}\n")
    return result


def solve_559():
    term = (a**(x**2) - b**(x**2))/(a**x - b**x)**2
    result = limit(term, x, a).doit()
    print(f"559: limit of {term} is {result}\n")
    return result


def solve_1203():
    f = x**2 * sin(a * x)
    result = diff(f, (x, n))
    print(f"1203: nth derivative of {f} is {result}")
    return result


def solve_1656():
    f = (2 * x - 3) ** 10
    result = integrate(f)
    print(f"1656: integral of {f} is {result} {simplify(result)}\n")
    return result


def solve_1657():
    f = root(1 - 3*x, 3)
    result = integrate(f)
    print(f"1657: integral of {f} is {result}\n")
    return result


def solve_1658():
    f = 1 / root(2 - 5*x, 2)
    result = integrate(f)
    print(f"1658: integral of {f} is {result}\n")
    return result


def solve_1807():
    f = log(x + root(1 + x**2, 2))
    result = integrate(f)
    print(f"1807: integral of {f} is {result}\n")
    return result


def solve_1808():
    f = x * log((1 + x) / (1 - x))
    result = integrate(f)
    print(f"1808: integral of {f} is {result}\n")
    return result


def solve_1809():
    f = atan(root(x, 2))
    result = integrate(f)
    print(f"1809: integral of {f} is {result}\n")
    return result


def solve_1810():
    f = sin(x) * log(tan(x))
    result = integrate(f)
    print(f"1810: integral of {f} is {result}\n")
    return result


def solve_3022():
    f = sin(2*n - 1)*x/(2*n - 1)
    s = summation(f, (n, 1, oo)).doit()
    print(f"3022: sum of {f} is {s} \n {s.subs(x, 1).doit()}\n")
    return s


def solve_3023():
    f = ((-1)**n) * (cos(n*x)/(n**2 - 1))
    s = summation(f, (n, 2, oo)).doit()
    print(f"3023: sum of {f} is {s} \n {s.subs(x, 1).doit()}\n")
    return s


def main() -> None:
    # solve_99()
    # solve_100()
    # solve_253()
    solve_279()
    # solve_299()
    # solve_555()
    # solve_556()
    # solve_557()
    # solve_558()
    # solve_559()
    # solve_1203()
    # solve_1656()
    # solve_1657()
    # solve_1658()
    # solve_1807()
    # solve_1808()
    # solve_1809()
    # solve_1810()
    # solve_3022()
    # solve_3023()


if __name__ == "__main__":
    main()
