from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    S: str = input()

    if S[0:4] == "YAKI":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
