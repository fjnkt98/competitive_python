from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(10000)
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
    N: int = int(input())
    E: List[Tuple[int, int, int]] = []
    for i in range(N):
        r: List[int] = list(map(int, input().split()))
        for (j, e) in enumerate(r):
            if e == -1:
                continue
            E.append((e, i, j))

    E.sort()

    uf = UnionFind(N)
    answer: int = 0
    for e in E:
        w, i, j = e

        if uf.is_same(i, j):
            continue

        answer += w
        uf.unite(i, j)

    print(answer)


if __name__ == "__main__":
    main()
