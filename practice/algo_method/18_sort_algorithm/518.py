from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    x: int = N // 2 - 1
    while x >= 0:
        k: int = x
        while 2 * k + 1 < N:
            kernel = [A[k], A[2 * k + 1]]
            if 2 * k + 2 < N:
                kernel.append(A[2 * k + 2])

            i = kernel.index(max(kernel))

            if i == 0:
                break
            elif i == 1:
                A[k], A[2 * k + 1] = A[2 * k + 1], A[k]
                k = 2 * k + 1
            else:
                A[k], A[2 * k + 2] = A[2 * k + 2], A[k]
                k = 2 * k + 2

        x -= 1

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
