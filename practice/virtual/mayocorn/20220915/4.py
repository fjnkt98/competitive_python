from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, Q = map(int, input().split())
    W, V = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    X: List[int] = list(map(int, input().split()))
    L, R = map(
        list, zip(*[list(map(lambda x: int(x) - 1, input().split())) for i in range(Q)])
    )

    C: List[Tuple[int, int]] = sorted([(v, w) for w, v in zip(W, V)], reverse=True)

    for l, r in zip(L, R):
        answer: int = 0
        B: List[int] = sorted([x for i, x in enumerate(X) if not l <= i <= r])
        used: List[int] = [False] * len(B)

        for v, w in C:
            for i in range(len(B)):
                if w <= B[i]:
                    answer += v
                    B.pop(i)
                    break

        print(answer)


if __name__ == "__main__":
    main()
