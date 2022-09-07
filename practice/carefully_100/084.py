from typing import *


def main():
    N, M = map(int, input().split())
    N = 5000
    G: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for i in range(M)]

    A: List[List[int]] = [[0 for j in range(i + 3)] for i in range(N + 2)]
    for a, b, x in G:
        a -= 1
        b -= 1

        A[a][b] += 1
        A[a][b + 1] -= 1
        A[a + x + 1][b] -= 1
        A[a + x + 2][b + 1] += 1
        A[a + x + 1][b + x + 2] += 1
        A[a + x + 2][b + x + 2] -= 1

    for i in range(N + 2):
        for j in range(1, i + 2):
            A[i][j] += A[i][j - 1]

    for i in range(1, N + 2):
        for j in range(i + 2):
            A[i][j] += A[i - 1][j]

    for i in range(1, N + 2):
        for j in range(1, i + 2):
            A[i][j] += A[i - 1][j - 1]

    answer: int = 0
    for a in A:
        answer += len(a) - a.count(0)

    print(answer)


if __name__ == "__main__":
    main()
