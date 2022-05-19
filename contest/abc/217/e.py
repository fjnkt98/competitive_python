from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    Q: int = int(input())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    A: Deque[int] = collections.deque()
    B: List[int] = []

    for q in query:
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            if B:
                print(heapq.heappop(B))
            else:
                print(A.popleft())
        else:
            while A:
                heapq.heappush(B, A.popleft())


if __name__ == "__main__":
    main()
