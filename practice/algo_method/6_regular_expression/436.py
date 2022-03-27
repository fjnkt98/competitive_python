from typing import List, Tuple
import sys
import collections
import itertools
import re


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()
    pattern = r"asian(?=(\w*\s){5,})"

    print(re.sub(pattern, "global", S))


if __name__ == "__main__":
    main()
