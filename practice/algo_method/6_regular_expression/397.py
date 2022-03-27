from typing import List, Tuple
import sys
import collections
import itertools
import re


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()
    pattern: str = r"ru(?=r)"

    print(re.sub(pattern, "ra", S))


if __name__ == "__main__":
    main()
