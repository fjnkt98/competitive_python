from typing import List
import sys
from array import array


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        u, k, *v = list(map(int, input().split()))
        graph[u - 1] = list(map(lambda x: x - 1, v))

    matrix: List[List[int]] = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for node in graph[i]:
            matrix[i][node] = 1

    for m in matrix:
        print(" ".join(map(str, m)))


if __name__ == "__main__":
    main()
