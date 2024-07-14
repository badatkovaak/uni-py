from sympy import  Matrix, root,solve, solve_linear_system, symbols
from numpy import array
from numpy.linalg import det, inv

# 6.9 г, 8.3 е, 13.1 з, 17.2 а, 18.3 к, 20.1 а, 22.7 з.

l = symbols('lambda')


def solve_6_9():
    a_1 = array([3, 2, 5])
    a_2 = array([2, 4, 7])
    a_3 = array([5, 6, l])
    b = array([1, 3, 5])

    M1 = Matrix([a_1, a_2, a_3])
    s = solve(M1.det(), l)
    
    print(f"\nvector {b} can be represented as a linear combination of \
{a_1}, {a_2}, {a_3} when lambda != {s[0]}\n")
    return s


def solve_8_3():
    A = Matrix([[3, -6, -1, 4, -7], [1, -2, -3, 7, -5], [2, -4, -14, 31, -18]])
    x, y, z, w = symbols('x y z w')
    
    s = solve_linear_system(A, x, y, z, w)
    if s is None:
        raise ValueError("This should never happen, here to satisfy typechecker")
    
    for i in [x, y, z, w]:
        if not s.get(i):
            s[i] = i
    
    print(f"\nsolution has form x = {s.get(x)}, y = {s.get(y)}, z = {s.get(z)}, w = {s.get(w)}\n")
    return s


def solve_13_1():
    A = array([[27, 44, 40, 55], [20, 64, 21, 40], [
              13, -20, -13, 24], [46, 45, -55, 84]])
    d = det(A)
    
    print(f"13.1: determinant of \n {A} is {d}\n")
    return d


def solve_17_2():
    A = array([[3, 0, 2, 0], [0, 1, 2, 1], [2, 3, 0, 0]])
    B = array([[1, -2, 2], [2, -1, 1], [-1, 1, -2], [2, 2, -1]])
    C = array([[-2, 0, -3], [0, 6, -3], [5, 2, 8]])
    result = A @ B + C
    
    print(f"17.2: \n{A}\n * \n{B}\n + \n{C}\n = \n{result}\n")
    return result


def solve_18_3():
    A = array([[1, 2, 1], [2, 1, 2], [1, 2, 3]])
    B = array([[2, 1, 0], [1, 1, 2], [-1, 2, 1]])
    X = inv(A) @ B
    
    print(f"18.3: X = \n{X}\n")
    return X


def solve_20_1():
    a = (2+1j)*(3-1j) + (2+3j)*(3+4j)
    
    print(f"20.1: (2+1j)*(3-1j) + (2+3j)*(3+4j) = {a}\n")
    return a


def solve_22_7():
    r = [root(-4, 4, i) for i in range(1, 5)]
    
    print(f"22.7: 4th roots of -4 are {r}\n")
    return r


def run_kostrikin() -> None:
    solve_6_9()
    solve_8_3()
    solve_13_1()
    solve_17_2()
    solve_18_3()
    solve_20_1()
    solve_22_7()


if __name__ == "__main__":
    run_kostrikin()
