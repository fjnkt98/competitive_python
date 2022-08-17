from typing import *
import collections
import itertools
import bisect
import math
import random
import time


def score(T: List[int], S: List[List[int]], C: List[int]) -> int:
    A: List[int] = [0] * len(T)
    L: List[int] = [-1] * 26
    for i, t in enumerate(T):
        L[t] = i
        A[i] = S[i][t] - sum([C[j] * (i - l) for j, l in enumerate(L)])

    return sum(A)


def main():
    start_time: float = time.time()

    D: int = int(input())
    C: List[int] = list(map(int, input().split()))
    S: List[List[int]] = [list(map(int, input().split())) for i in range(D)]

    H: List[List[int]] = [[-1] for i in range(26)]
    T: List[int] = [random.randint(0, 25) for _ in range(D)]
    for i, t in enumerate(T):
        H[t].append(i)
    for i in range(26):
        H[i].append(D)

    P: int = score(T, S, C)
    d2p: Dict[int, int] = {i: t for i, t in enumerate(T)}

    while time.time() - start_time < 1.8:
        d: int = random.randint(0, D - 1)
        q: int = random.randint(0, 25)

        p: int = d2p[d]

        index: int = bisect.bisect_left(H[p], d)
        k1: int = H[p][index - 1]
        k2: int = H[p][index + 1]
        index = bisect.bisect_left(H[q], d)
        l1: int = H[q][index - 1]
        l2: int = H[q][index]

        Q = (
            P
            - S[d][p]
            + S[d][q]
            - C[p] * (k2 - d) * (d - k1)
            + C[q] * (l2 - d) * (d - l1)
        )

        if Q > P:
            P = Q
            H[p].remove(d)
            bisect.insort_left(H[q], d)

            d2p[d] = q
        else:
            continue

    for i in range(D):
        print(d2p[i] + 1)


if __name__ == "__main__":
    main()
