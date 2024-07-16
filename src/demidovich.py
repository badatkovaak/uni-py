import sympy as s
import numpy as np
import matplotlib.pyplot as plt

# 99, 100, 253, 279 g, 299, 555-559, 1203, 1656-1658, 1807-1810, 3022, 3023


def solve_99():
    n = s.symbols("n", positive=True, integer=True)
    x = s.symbols("x", real=True)

    f = n**2 - 9 * n - 100
    min_value = s.minimum(f, n, s.Interval(1, s.oo, right_open=True))
    g = x**2 - 9 * x - 100 - min_value
    n_of_min_value = s.solve(g, x)[0]

    if abs(n_of_min_value - round(n_of_min_value)) >= 0.0000001:
        actual_min_value = min(
            f.subs({n: s.floor(n_of_min_value)}), f.subs({n: s.ceiling(n_of_min_value)})
        )
    else:
        actual_min_value = n_of_min_value

    print(f"\n99: минимум x_n = {f} это x = {actual_min_value}\n")
    return actual_min_value


def solve_100():
    n = s.symbols("n", positive=True, integer=True)
    x = s.symbols("x", real=True)

    f = n + 100 / n
    min_value = s.minimum(f, n, s.Interval(1, s.oo, right_open=True))
    g = x + 100 / x - min_value
    n_of_min_value = s.solve(g, x)[0]

    if abs(n_of_min_value - round(n_of_min_value)) >= 0.0000001:
        actual_min_value = min(
            f.subs({n: s.floor(n_of_min_value)}), f.subs({n: s.ceiling(n_of_min_value)})
        )
    else:
        actual_min_value = min_value

    print(f"\n100: минимум x_n = {f} это x = {actual_min_value}\n")
    return actual_min_value


def solve_253():
    x = np.arange(-5, 5, 0.01)
    y = (lambda x: x + 1 / x)(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r"$y = x + \frac{1}{x}$", color="b")

    plt.grid(True)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title(r"$y = x + \frac{1}{x}$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-100, 100)
    plt.legend(loc="upper right")

    # plt.show()

def solve_279():
    x = np.arange(-5, 5, 0.01)
    y = np.exp(1 / x**2)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r"$y = e^(\frac{1}{x^2})$", color="b")

    plt.grid(True)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title(r"$y = e^(\frac{1}{x^2})$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(0, 100)
    plt.legend(loc="upper right")

    # plt.show()


def solve_299():
    x = np.arange(-5, 5, 0.001)
    y = np.sin(1 / x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r"$y = \sin(\frac{1}{x})$", color="b")

    plt.grid(True)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title(r"$y = \sin(\frac{1}{x})$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper right")

    # plt.show()


def solve_555():
    n = s.symbols("n", positive=True, integer=True)
    a, b = s.symbols("a b", positive=True)

    term = ((s.root(a, n) + s.root(b, n)) / 2) ** n  # type: ignore
    result = s.limit(term, n, s.oo).doit()

    print(f"\n555: {result}\n")
    return result


def solve_556():
    x = s.symbols("x", real=True)
    a, b, c = s.symbols("a b c", positive=True)

    term = ((a**x + b**x + c**x) / 3) ** (1 / x)
    result = s.limit(term, x, 0).doit()

    print(f"\n556: {result}\n")
    return result


def solve_557():
    x = s.symbols("x", real=True)
    a, b, c = s.symbols("a b c", positive=True)

    term = ((a ** (x + 1) + b ** (x + 1) + c ** (x + 1)) / (a + b + c)) ** (1 / x)
    result = s.limit(term, x, 0).doit()

    print(f"\n557: {result}\n")
    return result


def solve_558():
    x = s.symbols("x", real=True)
    a, b = s.symbols("a b", positive=True)

    term = ((a ** (x**2) + b ** (x**2)) / (a**x + b**x)) ** (1 / x)
    result = s.limit(term, x, 0).doit()

    print(f"\n558: {result}\n")
    return result


def solve_559():
    x = s.symbols("x", real=True)
    a, b = s.symbols("a b", positive=True)

    term = (a ** (x**2) - b ** (x**2)) / (a**x - b**x) ** 2
    result = s.limit(term, x, a).doit()

    print(f"\n559: limit of {term} is {result}\n")
    return result


def solve_1203():
    x = s.symbols("x", real=True)
    a = s.symbols("a", positive=True)
    n = s.symbols("n", positive=True, integer=True)

    f = x**2 * s.sin(a * x)
    result = s.diff(f, (x, n))

    print(f"\n1203: n-ная производная {f} это \n{result}\n")
    return result


def solve_1656():
    x = s.symbols("x", real=True)
    f = (2 * x - 3) ** 10

    result = s.integrate(f)

    print(f"\n1656: интеграл {f} это \n{result} \n")
    return result


def solve_1657():
    x = s.symbols("x", real=True)
    f = s.root(1 - 3 * x, 3)

    result = s.integrate(f)

    print(f"\n1657: интеграл {f} это {result}\n")
    return result


def solve_1658():
    x = s.symbols("x", real=True)
    f = 1 / s.root(2 - 5 * x, 2)  # type: ignore

    result = s.integrate(f)

    print(f"\n1658: интеграл {f} это {result}\n")
    return result


def solve_1807():
    x = s.symbols("x", real=True)
    f = s.log(x + s.root(1 + x**2, 2))

    result = s.integrate(f)

    print(f"\n1807: интеграл {f} это {result}\n")
    return result


def solve_1808():
    x = s.symbols("x", real=True)
    f = x * s.log((1 + x) / (1 - x))

    result = s.integrate(f)

    print(f"\n1808: интеграл {f} это {result}\n")
    return result


def solve_1809():
    x = s.symbols("x", real=True)
    f = s.atan(s.root(x, 2))

    result = s.integrate(f)

    print(f"\n1809: интеграл {f} это {result}\n")
    return result


def solve_1810():
    x = s.symbols("x", real=True)
    f = s.sin(x) * s.log(s.tan(x))  # type: ignore

    result = s.integrate(f)

    print(f"\n1810: интеграл {f} это {result}\n")
    return result


def solve_3022():
    x = s.symbols("x", real=True)
    n = s.symbols("n", positive=True, integer=True)

    term = s.sin(2 * n - 1) * x / (2 * n - 1)
    sum = s.summation(term, (n, 1, s.oo)).doit()  # type: ignore

    print(f"\n3022: ряд {term} сходится к {sum}\n")  # type: ignore
    return sum


def solve_3023():
    x = s.symbols("x", real=True)
    n = s.symbols("n", positive=True, integer=True)

    term = ((-1) ** n) * (s.cos(n * x) / (n**2 - 1))
    sum = s.summation(term, (n, 2, s.oo)).doit()  # type: ignore

    print(f"\n3023: ряд {term} сходится к {sum}\n")  # type: ignore
    return sum


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
