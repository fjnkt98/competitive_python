from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


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
    N, M, K = map(int, input().split())
    uf = UnionFind(N)
    F: List[List[int]] = [[] for i in range(N)]
    B: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        F[a - 1].append(b - 1)
        F[b - 1].append(a - 1)
        uf.unite(a - 1, b - 1)
    for i in range(K):
        a, b = map(int, input().split())
        B[a - 1].append(b - 1)
        B[b - 1].append(a - 1)

    answer: List[int] = [0] * N
    for i in range(N):
        answer[i] = uf.get_size(i) - 1
        answer[i] -= len(F[i])
        for j in B[i]:
            if uf.is_same(i, j):
                answer[i] -= 1

    print(*answer)


if __name__ == "__main__":
    main()
