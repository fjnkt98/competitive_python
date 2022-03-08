from typing import List, Tuple, Deque
import sys
from array import array
import collections
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)
        graph[B - 1].append(A - 1)

    answer: int = 0
    for i in range(N):
        if bisect.bisect_left(sorted(graph[i]), i) == 1:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
