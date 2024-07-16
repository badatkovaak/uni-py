from numpy import allclose, array, eye, zeros
from numpy.linalg import eigvals, eigvalsh, solve, det
from numpy.typing import NDArray
from src.list_parser import parse


def is_diagonally_dominant(A: NDArray) -> bool:
    if A.shape[0] != A.shape[1]:
        raise ValueError
    
    for i in range(A.shape[1]):
        non_diagonal = 0
        for j in range(A.shape[0]):
            non_diagonal += (i != j) * abs(A[i][j])
        if non_diagonal >= abs(A[i][i]):
            return False
    
    return True


def solve_system_of_linear_equations_numerically(A: NDArray, B: NDArray) -> NDArray:
    match (A.shape, B.shape):
        case ((n, m), (k,)) if n == m == k:
            pass
        case _:
            raise ValueError("Некорректная размерность")
    
    if det(A) == 0:
        raise ValueError("Введенная матрица вырождена")

    if not is_diagonally_dominant(A):
        raise ValueError("Матрица не является диагонально преобладающей")
    
    M_inv = array(
        [
            [(lambda x, y: (x == y) * (1 / A[x][y]))(i, j) for j in range(A.shape[0])]
            for i in range(A.shape[0])
        ]
    )
    H = eye(A.shape[0]) - M_inv @ A
    G = M_inv @ B

    X = zeros(B.shape[0])
    for _ in range(30):
        X = H @ X + G
    return X


def run_test(A: NDArray, B: NDArray) -> None:
    s = solve_system_of_linear_equations_numerically(A, B)
    print("", A, B, s, solve(A, B), "", sep="\n")


def main() -> None:
    while True:
        command = input("""
    Введите 'tests' чтобы запустить тесты
    Введите 'keyboard' чтобы ввести матрицу вручную\n""")
        match command.replace("\n", "").replace(" ", "").lower():
            case "tests":
                tests()
            case "keyboard":
                try:
                    A = array(
                        parse(
                            input(
                                """\nВведите матрицу A 
примеры: [[1, 2], [3, 4]] ; (5, 6) ; {0.3} ; 5\n=>"""
                            )
                        )
                    )
                    B = array(
                        parse(
                            input(
                                """\nВведите вектор B
примеры: [[1, 2], [3, 4]] ; (5, 6) ; {0.3} ; 5\n=>"""
                            )
                        )
                    )
                    print("\n")
                    try:
                        result = solve_system_of_linear_equations_numerically(A, B)
                    except ValueError as e:
                        print(f"\nОшибка: {e}\n")
                        continue
                    print(
                        f"\nВычисленный результат - {result}, настоящий - {solve(A,B)}\n"
                    )
                except ValueError as e:
                    print(f"Ошибка: {e}\n")
                    continue
            case _:
                print("Неизвестная команда\n")
                continue


def tests() -> None:
    A0, B0 = (
        array(
            [
                [68, 16, 8, -15],
                [-16, 123, -11, 21],
                [-5, 8, 100, -34],
                [-12, -14, 18, 94],
            ]
        ),
        array([242, 143, -16, 162]),
    )
    A1, B1 = array([[1, 2, 3], [3, 4, 5], [4, 5, 7]]), array([1, 2, 3])
    A2, B2 = array([[1, 2], [3, 4]]), array([2, 2])
    A3, B3 = array([[3, 4], [-1, 2]]), array([1, 3])
    A4, B4 = array([[-1, 2], [3, 4]]), array([1, 3])
    A5, B5 = array([[1, 5], [5, 1]]), array([5, 7])

    run_test(A0, B0)
    run_test(A1, B1)
    run_test(A2, B2)
    run_test(A3, B3)
    run_test(A4, B4)
    run_test(A5, B5)


if __name__ == "__main__":
    main()
