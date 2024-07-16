import sympy as s
import numpy as np

# 6.9 г, 8.3 е, 13.1 з, 17.2 а, 18.3 к, 20.1 а, 22.7 з.


def solve_6_9():
    lambda_ = s.symbols("l")
    a_1 = np.array([3, 2, 5])
    a_2 = np.array([2, 4, 7])
    a_3 = np.array([5, 6, lambda_])
    b = np.array([1, 3, 5])

    M1 = s.Matrix([a_1, a_2, a_3])
    solution = s.solve(M1.det(), lambda_)

    print(f"\n6.9: вектор {b} может быть представлен как линейная комбинация \
{a_1}, {a_2}, {a_3} когда lambda != {solution[0]}\n")
    return solution


def solve_8_3():
    A = s.Matrix([[3, -6, -1, 4, -7], [1, -2, -3, 7, -5], [2, -4, -14, 31, -18]])
    x, y, z, w = s.symbols("x y z w")

    solution = s.solve_linear_system(A, x, y, z, w)
    if solution is None:
        raise ValueError("Should never happen")

    for i in [x, y, z, w]:
        if not solution.get(i):
            solution[i] = i

    print(
        f"\n8.3: общее решение имеет вид x = {solution.get(x)},\
 y = {solution.get(y)}, z = {solution.get(z)}, w = {solution.get(w)}\n"
    )
    return solution


def solve_13_1():
    A = np.array(
        [[27, 44, 40, 55], [20, 64, 21, 40], [13, -20, -13, 24], [46, 45, -55, 84]]
    )
    determinant = np.linalg.det(A)

    print(f"\n13.1: определитель \n {A} это {determinant}\n")
    return determinant


def solve_17_2():
    A = np.array([[3, 0, 2, 0], [0, 1, 2, 1], [2, 3, 0, 0]])
    B = np.array([[1, -2, 2], [2, -1, 1], [-1, 1, -2], [2, 2, -1]])
    C = np.array([[-2, 0, -3], [0, 6, -3], [5, 2, 8]])
    result = A @ B + C

    print(f"\n17.2: \n{A}\n * \n{B}\n + \n{C}\n = \n{result}\n")
    return result


def solve_18_3():
    A = np.array([[1, 2, 1], [2, 1, 2], [1, 2, 3]])
    B = np.array([[2, 1, 0], [1, 1, 2], [-1, 2, 1]])
    X = np.linalg.inv(A) @ B

    print(f"\n18.3: X = \n{X}\n")
    return X


def solve_20_1():
    num = (2 + 1j) * (3 - 1j) + (2 + 3j) * (3 + 4j)

    print(f"\n20.1: (2+1j)*(3-1j) + (2+3j)*(3+4j) = {num}\n")
    return num


def solve_22_7():
    roots = [s.root(-4, 4, i) for i in range(1, 5)]

    print(f"\n22.7: корни 4 степени от -4 -  {roots}\n")
    return roots


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
