from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: List[int] = list(map(int, input().split()))
    Q: int = int(input())
    T: List[int] = list(map(int, input().split()))

    S = set(S)
    answer: int = 0
    for t in T:
        if t in S:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
