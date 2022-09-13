from typing import *
import collections
import itertools
import bisect
import math
import copy


def main():
    N: int = int(input())

    if N == 1:
        print("Yes")
        print(2)
        print(1, 1)
        print(1, 1)
        return

    A: List[int] = [k * (k - 1) // 2 for k in range(2 * N)]

    if N not in A:
        print("No")
        return

    K: int = A.index(N)
    B: List[List[int]] = [
        [i * (i + 1) // 2 + j + 1 for j in range(i + 1)] for i in range(K - 1)
    ]

    S: List[List[int]] = []
    for i in range(K - 1):
        s: List[int] = copy.copy(B[i])
        for j in range(i + 1, K - 1):
            s.append(B[j][len(B[i]) - 1])

        S.append(s)
    S.append([b[-1] for b in B])

    print("Yes")
    print(K)
    for s in S:
        print(len(s), *s)


if __name__ == "__main__":
    main()
