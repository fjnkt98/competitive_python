from typing import *
import collections
import itertools
import bisect
import math
import operator


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


def dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return min(abs(x1 - x2), abs(y1 - y2))


def main():
    N: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    edges: List[Tuple[int, int, int]] = []
    A = sorted(list(enumerate(X)), key=operator.itemgetter(1))
    B = sorted(list(enumerate(Y)), key=operator.itemgetter(1))
    for i in range(N - 1):
        a: int = A[i][0]
        b: int = A[i + 1][0]
        edges.append((a, b, dist(X[a], Y[a], X[b], Y[b])))
    for i in range(N - 1):
        a: int = B[i][0]
        b: int = B[i + 1][0]
        edges.append((a, b, dist(X[a], Y[a], X[b], Y[b])))

    edges.sort(key=operator.itemgetter(2))

    uf = UnionFind(N)
    answer: int = 0
    for a, b, w in edges:
        if not uf.is_same(a, b):
            uf.unite(a, b)
            answer += w

    print(answer)


if __name__ == "__main__":
    main()
