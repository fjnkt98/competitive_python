from typing import List, Tuple, DefaultDict
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    S: str = input().rstrip()

    D: DefaultDict[List[List[int]]] = collections.defaultdict(list)
    for i, p in enumerate(P):
        x, y = p
        D[y].append([i, x])

    ok: bool = False
    for d in D.values():
        d.sort(key=lambda x: x[1])

        colide: bool = False
        right: bool = False
        for i, x in d:
            if S[i] == "R":
                right = True
            elif right:
                colide = True

        if colide:
            ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
