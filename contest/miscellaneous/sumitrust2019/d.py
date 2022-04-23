from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    S: str = input()

    answer: int = 0
    for x in range(0, 1000):
        y: str = str(x).zfill(3)
        i: int = 0
        ok: List[bool] = [False] * 3
        for j, s in enumerate(S):
            if s == y[i]:
                ok[i] = True
                i += 1

            if i >= 3:
                break

        if all(ok):
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
