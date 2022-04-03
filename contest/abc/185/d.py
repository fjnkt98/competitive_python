from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    if not A:
        print(1)
        return

    A.sort()
    A.insert(0, 0)
    A.append(N + 1)
    diff: List[int] = []
    for i in range(len(A) - 1):
        d: int = A[i + 1] - A[i] - 1
        if d != 0:
            diff.append(d)

    if len(diff) == 0:
        print(0)
        return

    k: int = min(diff)

    answer: int = 0
    for d in diff:
        answer += d // k

        if d % k != 0:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
