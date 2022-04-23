from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    mod: int = 1000000007
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: int = 1
    count: List[int] = [0] * (N + 1)
    count[0] = 3
    for i, a in enumerate(list(map(lambda x: x + 1, A))):
        if count[a - 1] > 0:
            answer *= count[a - 1]
            answer %= mod

            count[a - 1] -= 1
            count[a] += 1
        else:
            print(0)
            return

    print(answer % mod)


if __name__ == "__main__":
    main()
