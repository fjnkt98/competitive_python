from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    A: List[int] = [int(input()) for i in range(N)]

    answer: int = 0
    B: List[List[int]] = []
    buff: List[int] = []
    for a in A:
        if a == 0:
            if buff:
                B.append(buff)
                buff = []
        else:
            buff.append(a)
    B.append(buff)

    for b in B:
        answer += sum(b) // 2

    print(answer)


if __name__ == "__main__":
    main()
