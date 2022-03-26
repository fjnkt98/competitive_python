from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def check(S: str) -> bool:
    depth: int = 0
    for s in S:
        if s == "(":
            depth += 1
        elif s == ")":
            depth -= 1

        if depth < 0:
            return False

    return True if depth == 0 else False


def main():
    N: int = int(input())

    for p in itertools.product(["(", ")"], repeat=N):
        if check("".join(p)):
            print("".join(p))


if __name__ == "__main__":
    main()
