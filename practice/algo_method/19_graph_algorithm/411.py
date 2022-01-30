from typing import List
from sys import setrecursionlimit

setrecursionlimit(10000)


def main():
    N, A, B = map(int, input().split())
    G: List[List[str]] = [[] for i in range(N)]

    for i in range(N):
        S: str = input()
        G[i] = list(S)

    if G[A][B] == "o":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
