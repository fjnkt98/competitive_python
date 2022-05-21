from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    counter = collections.Counter(A)
    B: List[int] = [0 for i in range(max(A) + 2)]
    for k, v in counter.items():
        B[k + 1] = v

    B = list(itertools.accumulate(B))

    answer: int = 0
    for j, a in enumerate(A):
        x: int = B[a]
        y: int = N - B[a] - counter[a]

        answer += x * y

    print(answer)


if __name__ == "__main__":
    main()
