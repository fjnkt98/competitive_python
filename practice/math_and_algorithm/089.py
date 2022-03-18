from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    ok: bool = False

    if c == 1:
        ok = False
    else:
        r: int = 1
        for i in range(b):
            r *= c
            if a < r:
                ok = True
                break

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
