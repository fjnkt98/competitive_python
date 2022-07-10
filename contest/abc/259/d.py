from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


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


def dist_sq(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x1, y1 = p1
    x2, y2 = p2

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def is_cross(p1: Tuple[int, int, int], p2: Tuple[int, int, int]) -> bool:
    x1, y1, r1 = p1
    x2, y2, r2 = p2

    d: int = dist_sq((x1, y1), (x2, y2))

    if d == r2 ** 2 - 2 * r1 * r2 + r1 ** 2:
        return True
    elif d > r2 ** 2 - 2 * r1 * r2 + r1 ** 2:
        if d <= r2 ** 2 + 2 * r1 * r2 + r1 ** 2:
            return True
        else:
            return False
    else:
        return False


def main():
    N: int = int(input())
    sx, sy, tx, ty = map(int, input().split())
    P: List[Tuple[int, int]] = [list(map(int, input().split())) for i in range(N)]

    uf = UnionFind(N)
    for i, j in itertools.combinations(range(N), r=2):
        if is_cross(P[i], P[j]):
            uf.unite(i, j)

    for i, p in enumerate(P):
        x, y, r = p
        if dist_sq((x, y), (sx, sy)) == r ** 2:
            s = i
        if dist_sq((x, y), (tx, ty)) == r ** 2:
            t = i

    if uf.is_same(s, t):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
