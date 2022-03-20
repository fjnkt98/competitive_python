from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()

    if len(S) == 26:
        T: List[str] = []
        s: str = chr(ord("a") - 1)
        for c in reversed(S):
            if c > s:
                T.append(c)
                s = c
            else:
                break

        if len(T) == 26:
            print(-1)
            return

        i: int = len(S) - len(T)

        print(S[: i - 1] + min(list(filter(lambda x: x > S[i - 1], T))))
    else:
        available: Set = {chr(ord("a") + i) for i in range(26)}
        available = available - set(S)

        print(S + min(available))


if __name__ == "__main__":
    main()
