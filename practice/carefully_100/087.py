from typing import *
import collections
import itertools
import bisect
import math


class UnionFind:
    """Union-Find Tree

    Class implementation of disjoint-set data structure

    Attributes:
        _parent (List[int]): A list retaining the parent of the node.
        _rank (List[int]): A list retaining rank of the subtree to which
        the node belongs.
        _size (List[int]): A list retaining the size of the subtree to
        which the node belongs.
    """

    def __init__(self, N: int):
        """Constructor

        Arg:
            N (int): Number of nodes.
        """
        self._parent: List[int] = [-1 for i in range(N)]
        self._rank: List[int] = [0 for i in range(N)]
        self._size: List[int] = [1 for i in range(N)]

    def get_root(self, x: int) -> int:
        """Return the root of the tree to which x belongs

        Arg:
            x (int): Index of the node.

        Return:
            int: Index of the root of the node.
        """
        if self._parent[x] == -1:
            return x
        else:
            self._parent[x] = self.get_root(self._parent[x])
            return self._parent[x]

    # Return true if x and y belong to the same tree
    def is_same(self, x: int, y: int) -> bool:
        """Return true if x and y belong to the same subtree.

        Args:
            x (int): Index of the node.
            y (int): Index of the other node.

        Return:
            bool: True when two  nodes belong to the same subtree, false otherwise
        """
        return self.get_root(x) == self.get_root(y)

    def unite(self, x: int, y: int) -> bool:
        """Merge the group to which x belongs and the group to which y belongs

        Args:
            x (int): Index of the node.
            y (int): Index of the other node.

        Return:
            bool: True when two nodes have successfully merged,
            false when two nodes has been already belong same subtree.
        """
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

    def get_size(self, x: int) -> int:
        """Return size of the subtree to which x belongs.

        Args:
            x (int): Index of the node.

        Return:
            int: Size of the subtree to which x belongs.

        """

        return self._size[self.get_root(x)]


def main():
    N, M = map(int, input().split())
    E: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(M)]

    uf = UnionFind(N)

    answer: List[int] = [0 for i in range(M)]
    for i, (a, b) in enumerate(reversed(E)):
        a -= 1
        b -= 1
        if uf.is_same(a, b):
            uf.unite(a, b)
            answer[i] = 0
        else:
            answer[i] = uf.get_size(a) * uf.get_size(b)
            uf.unite(a, b)

    for a in itertools.accumulate(reversed(answer)):
        print(a)


if __name__ == "__main__":
    main()
