from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    L: int = 1010

    grid: List[List[int]] = [[0] * (L) for i in range(L)]

    for lx, ly, rx, ry in P:
        grid[lx][ly] += 1
        grid[rx][ry] += 1
        grid[lx][ry] -= 1
        grid[rx][ly] -= 1

    for j in range(0, L):
        for i in range(1, L):
            grid[i][j] += grid[i - 1][j]

    for i in range(0, L):
        for j in range(1, L):
            grid[i][j] += grid[i][j - 1]

    answer: List[int] = [0] * (N + 1)
    for i in range(0, L):
        for j in range(0, L):
            answer[grid[i][j]] += 1

    for a in answer[1:]:
        print(a)


if __name__ == "__main__":
    main()
