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


def dist(
    x1: float,
    y1: float,
    z1: float,
    r1: float,
    x2: float,
    y2: float,
    z2: float,
    r2: float,
) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) - r1 - r2


def main():
    until: bool = True
    results: List[int] = []
    while until:
        N: int = int(input())
        if N == 0:
            until = False
            break
        X, Y, Z, R = map(
            list, zip(*[list(map(float, input().split())) for i in range(N)])
        )

        edges: List[Tuple[int, int, float]] = []
        for i, j in itertools.combinations(range(N), r=2):
            d: float = dist(X[i], Y[i], Z[i], R[i], X[j], Y[j], Z[j], R[j])

            edges.append((i, j, max(d, 0.0)))

        edges.sort(key=operator.itemgetter(2))

        uf = UnionFind(N)
        answer: float = 0.0
        for i, j, d in edges:
            if uf.is_same(i, j):
                continue
            else:
                uf.unite(i, j)
                answer += d

        results.append(answer)

    for r in results:
        print("{:.3f}".format(r))


if __name__ == "__main__":
    main()
