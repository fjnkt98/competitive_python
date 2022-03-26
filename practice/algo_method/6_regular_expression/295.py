from typing import List, Tuple
import sys
import collections
import itertools
import re


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()
    pattern: str = r"^\d{3}\-\d{4}$"

    print("Yes" if re.search(pattern, S) else "No")


if __name__ == "__main__":
    main()
