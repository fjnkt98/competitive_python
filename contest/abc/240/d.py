from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    P: List[List[int, int]] = []
    answer: int = 0
    for a in A:
        if P:
            p: List[int] = P[-1]
            if a == p[0]:
                p[1] += 1
                answer += 1
                if p[1] == a:
                    answer -= p[1]
                    P.pop()
                print(answer)

            else:
                P.append([a, 1])
                answer += 1
                print(answer)
        else:
            P.append([a, 1])
            answer += 1
            print(answer)


if __name__ == "__main__":
    main()
