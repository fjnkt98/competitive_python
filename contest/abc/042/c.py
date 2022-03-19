from typing import List, Tuple, Set
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    D: List[int] = list(map(int, input().split()))

    A: Set[int] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set(D)

    for i in range(N, 10000000):
        S: Set[int] = set(str(i))
        ok: bool = True
        for d in D:
            if str(d) in S:
                ok = False

        if ok:
            print(i)
            return


if __name__ == "__main__":
    main()
