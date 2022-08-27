from typing import *
import collections
import itertools
import bisect
import math


class UnionFind:
    """
    Class implementation of disjoint-set data structure
    """

    # Constructor
    def __init__(self, N: int):
        self._parent: List[int] = [-1 for i in range(N)]
        self._rank: List[int] = [0 for i in range(N)]
        self._size: List[int] = [1 for i in range(N)]

    # Return the root of the tree to which x is belonging
    def get_root(self, x: int) -> int:
        if self._parent[x] == -1:
            return x
        else:
            self._parent[x] = self.get_root(self._parent[x])
            return self._parent[x]

    # Return true if x and y belong to the same tree
    def is_same(self, x: int, y: int) -> bool:
        return self.get_root(x) == self.get_root(y)

    # Merge the group to which x is belonging and the group to which y is belonging
    def unite(self, x: int, y: int) -> bool:
        # Get root of x and y
        rx = self.get_root(x)
        ry = self.get_root(y)

        # Do nothing when x and y are already in same group
        if rx == ry:
            return False

        # Union by rank
        # Make sure that the rank of ry side is small
        if self._rank[rx] < self._rank[ry]:
            rx, ry = ry, rx

        # Make sure that ry is child of rx
        self._parent[ry] = rx

        # Compute rank of rx side
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1

        # Compute size of rx side
        self._size[rx] += self._size[ry]

        return True

    # Return size of the group to which x is belonging
    def get_size(self, x: int) -> int:
        return self._size[self.get_root(x)]


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    indegree: List[int] = [0] * N
    for i in range(N):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        indegree[u] += 1
        indegree[v] += 1

    in_cycle: List[bool] = [len(g) != 1 for i, g in enumerate(graph)]
    candidate = collections.deque([i for i, g in enumerate(graph) if len(g) == 1])
    while candidate:
        node: int = candidate.popleft()
        for next_node in graph[node]:
            if not in_cycle[next_node]:
                continue
            indegree[next_node] -= 1
            if indegree[next_node] <= 1:
                in_cycle[next_node] = False
                candidate.append(next_node)

    uf = UnionFind(N)
    cycle: Set[int] = {i for i, b in enumerate(in_cycle) if b}
    explored: List[bool] = [False] * N
    for start in cycle:
        candidate = collections.deque([start])
        explored[start] = True

        while candidate:
            node: int = candidate.popleft()

            for next_node in graph[node]:
                if next_node in cycle or explored[next_node]:
                    continue
                explored[next_node] = True
                candidate.append(next_node)
                uf.unite(start, next_node)

    Q: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))
    for x, y in zip(X, Y):
        x -= 1
        y -= 1

        if x in cycle and y in cycle:
            print("No")
        elif uf.is_same(x, y):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
