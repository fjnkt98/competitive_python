from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = [0] * M
    B: List[int] = [0] * M
    indegree: List[int] = [0] * N
    outdegree: List[int] = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A[i] = a
        B[i] = b
        indegree[b] += 1
        outdegree[a] += 1

    if all(map(lambda x: x % 2 == 0, [a + b for a, b in zip(indegree, outdegree)])):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
