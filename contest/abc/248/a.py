from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    S: str = input()

    T: Set[int] = {str(i) for i in range(10)}
    T = T - set(S)

    print(T.pop())


if __name__ == "__main__":
    main()
