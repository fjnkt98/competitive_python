from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    T: List[int] = [int(input()) for i in range(N)]

    T.sort()

    mod: int = 1000000007

    factorial: List[int] = [1] * (10001)
    for i in range(2, 10001):
        factorial[i] = i * factorial[i - 1] % mod

    answer: int = 1
    for k, v in itertools.groupby(T):
        answer *= factorial[len(list(v))]
        answer %= mod

    print(sum(list(itertools.accumulate(T))))
    print(answer)


if __name__ == "__main__":
    main()
