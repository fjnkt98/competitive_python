from typing import List
from sys import setrecursionlimit


setrecursionlimit(10000)


def main():
    N, M = map(int, input().split())
    G: List[List[int]] = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        G[A].append(B)

    for g in G:
        if g:
            print(" ".join(map(str, sorted(g))))
        else:
            print("")


if __name__ == "__main__":
    main()
