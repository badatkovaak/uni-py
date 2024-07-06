import numpy.typing as nt
from numpy import allclose, array, eye, zeros
from numpy.linalg import eigvals, eigvalsh, solve, det


def spectral_radius(A: nt.NDArray) -> float:
    return abs(max(eigvals(A), key=lambda x: abs(x)))


def spectral_radius_h(A: nt.NDArray) -> float:
    return abs(max(eigvalsh(A), key=lambda x: abs(x)))


def is_diagonally_dominant(A: nt.NDArray) -> bool:
    if A.shape[0] != A.shape[1]:
        raise ValueError
    for i in range(A.shape[1]):
        non_diagonal = 0
        for j in range(A.shape[0]):
            non_diagonal += (i != j)*abs(A[i][j])
        if non_diagonal >= abs(A[i][i]):
            return False
    return True


def is_hermitian(A: nt.NDArray) -> bool:
    return allclose(A, A.conjugate().transpose(), atol=0.000001)


def approximate_system_of_linear_eqs(A: nt.NDArray, B: nt.NDArray) -> nt.NDArray:
    match (A.shape, B.shape):
        case ((n, m), (k,)) if m == k and n != 0:
            pass
        case _:
            raise ValueError("Incorrect Dimensions")
    if det(A) == 0:
        raise ValueError("Input Matrix is Singular")

    X = zeros(B.shape[0])
    if is_diagonally_dominant(A):
        M = array([[(lambda x, y: (x == y) * A[x][y])(i, j)
                    for j in range(A.shape[0])] for i in range(A.shape[0])])
        M_inv = array([[(lambda x, y: (x == y)*(1/A[x][y]))(i, j)
                        for j in range(A.shape[0])] for i in range(A.shape[0])])
        H = eye(A.shape[0]) - M_inv @ A
        G = M_inv @ B
        # print(M, A, M_inv, H,  sep='\n', end='\n\n')
    elif is_hermitian(A):
        l_min, l_max = (lambda x: (x[0], x[-1]))(sorted(eigvalsh(A)))
        alpha = 2/(l_min + l_max)
        H = eye(A.shape[0]) - alpha * A
        G = alpha * B
    else:
        M = array([[(lambda x, y: (x == y) * A[x][y])(i, j)
                    for j in range(A.shape[0])] for i in range(A.shape[0])])
        M_inv = array([[(lambda x, y: (x == y)*(1/A[x][y]))(i, j)
                        for j in range(A.shape[0])] for i in range(A.shape[0])])
        H = M_inv @ (M - A)
        G = M_inv @ B
        # print(M, A, M_inv, H,  sep='\n', end='\n\n')
    print(f"is diagonally dominant - {is_diagonally_dominant(A)}")
    print(f"spectral radius of H is {spectral_radius(H)}")

    for _ in range(20):
        X = H @ X + G
    return X


def main():
    A0, B0 = array([[68, 16, 8, -15], [-16, 123, -11, 21], [-5, 8, 100, -34],
                    [-12, -14, 18, 94]]), array([242, 143, -16, 162])
    A1, B1 = array([[1, 2, 3], [3, 4, 5], [4, 5, 7]]), array([1, 2, 3])
    A2, B2 = array([[1, 2], [3, 4]]), array([2, 2])
    A3, B3 = array([[3, 4], [-1, 2]]), array([1, 3])
    A4, B4 = array([[-1, 2], [3, 4]]), array([1, 3])
    A5, B5 = array([[2, 1], [1, 2]]), array([5, 7])
    # s1 = approximate_system_of_linear_eqs(A1, B1)
    # s2 = approximate_system_of_linear_eqs(A2, B2)
    # s3 = approximate_system_of_linear_eqs(A3, B3)
    # s4 = approximate_system_of_linear_eqs(A4, B4)
    # s5 = approximate_system_of_linear_eqs(A5, B5)
    s0 = approximate_system_of_linear_eqs(A0, B0)
    print(s0)
    print(solve(A0, B0))
    # print(s1)
    # print(solve(A1, B1))
    # print(s2)
    # print(solve(A2, B2))
    # print(s3)
    # print(solve(A3, B3))
    # print(s4)
    # print(solve(A4, B4))
    # print(s5)
    # print(solve(A5, B5))


if __name__ == "__main__":
    main()
