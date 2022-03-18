from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: str = input().rstrip()

    depth: int = 0
    for c in S:
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1

        if depth < 0:
            print("No")
            return

    if depth != 0:
        print("No")
        return

    print("Yes")
    return


if __name__ == "__main__":
    main()
