from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    query: List[Tuple[int, int, int]] = [() for i in range(Q)]
    for i in range(Q):
        l, r, x = map(int, input().split())
        query[i] = (l - 1, r - 1, x)

    A: List[int] = [0 for i in range(N + 1)]
    for l, r, x in query:
        A[l] += x
        A[r + 1] -= x

    C = list(itertools.accumulate(A))
    answer: List[str] = ["" for i in range(N - 1)]
    for i in range(N - 1):
        if C[i] == C[i + 1]:
            answer[i] = "="
        elif C[i] > C[i + 1]:
            answer[i] = ">"
        else:
            answer[i] = "<"

    print("".join(answer))


if __name__ == "__main__":
    main()
