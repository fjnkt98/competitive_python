from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    graph: List[List[bool]] = [[False] * N for i in range(N)]
    for x, y in [map(int, input().split()) for i in range(M)]:
        graph[x - 1][y - 1] = True
        graph[y - 1][x - 1] = True

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=N):
        mans: List[int] = [i for i, bit in enumerate(bits) if bit == 1]
        ok: bool = True
        for i, j in itertools.combinations(mans, 2):
            if not graph[i][j]:
                ok = False

        if ok:
            answer = max(answer, len(mans))

    print(answer)


if __name__ == "__main__":
    main()
