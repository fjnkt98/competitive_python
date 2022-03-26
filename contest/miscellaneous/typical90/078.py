from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    answer: int = 0
    for i in range(N):
        if bisect.bisect_left(sorted(graph[i]), i) == 1:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
