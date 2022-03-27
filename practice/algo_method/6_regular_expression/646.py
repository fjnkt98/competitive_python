from typing import List, Tuple
import sys
import collections
import itertools
import re


sys.setrecursionlimit(1000000)


def main():
    N, Y, M = map(int, input().split())
    S: List[str] = [input() for i in range(N)]

    pattern: str = f"^{Y}{str(M).zfill(2)}"
    for s in S:
        t: List[str] = s.split("_")

        if re.search(pattern, t[2]):
            print(t[1])


if __name__ == "__main__":
    main()
