from typing import *
import collections
import itertools
import bisect
import math


def score(T: List[int], S: List[List[int]], C: List[int]) -> List[int]:
    A: List[int] = [0] * len(T)
    L: List[int] = [-1] * 26
    for i, t in enumerate(T):
        L[t] = i
        A[i] = S[i][t] - sum([C[j] * (i - l) for j, l in enumerate(L)])

    return list(itertools.accumulate(A))


def main():
    D: int = int(input())
    C: List[int] = list(map(int, input().split()))
    S: List[List[int]] = [list(map(int, input().split())) for i in range(D)]
    T: List[int] = [int(input()) - 1 for i in range(D)]
    M: int = int(input())
    E, Q = map(list, zip(*[[int(x) - 1 for x in input().split()] for i in range(M)]))

    H: List[List[int]] = [[-1] for i in range(26)]
    for i, t in enumerate(T):
        H[t].append(i)
    for i in range(26):
        H[i].append(D)

    P = score(T, S, C)[-1]
    d_to_p: Dict[int, int] = {i: t for i, t in enumerate(T)}

    A: List[int] = [0] * M
    for i, (d, q) in enumerate(zip(E, Q)):
        p: int = d_to_p[d]
        index: int = bisect.bisect_left(H[p], d)
        k1: int = H[p][index - 1]
        k2: int = H[p][index + 1]
        index = bisect.bisect_left(H[q], d)
        l1: int = H[q][index - 1]
        l2: int = H[q][index]

        A[i] = P if i == 0 else A[i - 1]
        A[i] += (
            -S[d][p] + S[d][q] - C[p] * (k2 - d) * (d - k1) + C[q] * (l2 - d) * (d - l1)
        )

        H[p].remove(d)
        bisect.insort_left(H[q], d)

        d_to_p[d] = q

    for a in A:
        print(a)


if __name__ == "__main__":
    main()
