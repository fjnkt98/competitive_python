from multiprocessing.spawn import import_main_path

from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    S: str = input()

    small: bool = False
    capital: bool = False
    unique: bool = True

    count = collections.Counter(S)

    for key, value in count.items():
        if key.islower():
            small = True
        if key.isupper():
            capital = True

        if value != 1:
            unique = False

    if all((small, capital, unique)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
