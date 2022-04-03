from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    S: List[str] = [input() for i in range(N)]

    P: Set[str] = set(map(lambda s: s[1:], filter(lambda s: s[0] == "!", S)))
    Q: Set[str] = set(filter(lambda s: s[0] != "!", S))

    R: Set[str] = P.intersection(Q)
    if R:
        print(R.pop())
    else:
        print("satisfiable")


if __name__ == "__main__":
    main()
