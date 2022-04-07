from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: int = 0
    C = collections.Counter(A)
    S: List[int] = []
    for k, v in C.items():
        if v >= 4:
            S.append(k)
            S.append(k)
        elif v >= 2:
            S.append(k)

    S.sort(reverse=True)
    if len(S) < 2:
        print(0)
    else:
        print(S[0] * S[1])


if __name__ == "__main__":
    main()
