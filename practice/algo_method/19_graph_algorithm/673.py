from typing import List
from sys import setrecursionlimit


setrecursionlimit(10000)


def main():
    N, M = map(int, input().split())
    G: List[List[int]] = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)

    answer: int = N
    amount: int = 0
    for i in reversed(range(N)):
        if amount <= len(G[i]):
            amount = len(G[i])
            answer = min(answer, i)

    print(" ".join(map(str, sorted(G[answer]))))


if __name__ == "__main__":
    main()
