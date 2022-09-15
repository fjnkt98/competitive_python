from typing import *
import copy


def main():
    W: int = int(input())
    N, K = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp1: List[List[int]] = [[0] * (K + 1) for i in range(W + 1)]
    dp2: List[List[int]] = [[0] * (K + 1) for i in range(W + 1)]

    positive: bool = True
    for i in range(1, N + 1):
        if positive:
            for j in range(W + 1):
                for k in range(1, K + 1):
                    dp1[j][k] = dp2[j][k]

                    if j - A[i - 1] >= 0:
                        dp1[j][k] = max(dp1[j][k], dp2[j - A[i - 1]][k - 1] + B[i - 1])
            positive = not positive
        else:
            for j in range(W + 1):
                for k in range(1, K + 1):
                    dp2[j][k] = dp1[j][k]

                    if j - A[i - 1] >= 0:
                        dp2[j][k] = max(dp2[j][k], dp1[j - A[i - 1]][k - 1] + B[i - 1])
            positive = not positive

    if positive:
        print(dp2[W][K])
    else:
        print(dp1[W][K])


if __name__ == "__main__":
    main()
