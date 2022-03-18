from typing import List, Tuple
import sys
from array import array
import numpy as np

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    Q: int = int(input())
    answer: List[str] = []
    for i in range(Q):
        X, Y, Z, T = input().split()
        X, Y, Z = map(float, (X, Y, Z))
        T = int(T)

        A = np.array([[1 - X, Y, 0], [0, 1 - Y, Z], [X, 0, 1 - Z]])

        result: np.ndarray = np.linalg.matrix_power(A, T)
        # print(f"{sum(answer[0]):.8f} {sum(answer[1]):.8f} {sum(answer[2]):.8f}")
        answer.append(f"{sum(result[0]):.8f} {sum(result[1]):.8f} {sum(result[2]):.8f}")

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
