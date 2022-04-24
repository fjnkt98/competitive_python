from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# Type of the weight for Weighted Union-Find Tree
T = TypeVar("T", int, float)


class WeightedUnionFind(Generic[T]):
    """Weighted Union-Find Tree

    Attributes:
        _N (int): Number of nodes.
        _e (T): Identity element of the abelian group. Normally assigned 0.
        _parent (List[int]): List retaining the parent node of the node.
        _rank (List[int]): List retaining the rank of the node.
        _diff_weight (List[T]): List retaining the weight difference
                                between the root of the subtree.

    """

    def __init__(self, N: int, e: T):
        """Constructor

        Args:
            N (int): Number of nodes.
            e (T): Identity element of the abelian group. Normally assigned 0.

        """
        self._N: int = N
        self._e: T = e
        self._parent: List[int] = [i for i in range(N)]
        self._rank: List[int] = [0 for i in range(N)]
        self._diff_weight: List[T] = [e for i in range(N)]

    def root(self, v: int) -> int:
        """Returns the root.

        Returns the root of the subtree to which the node v is belonging.
        In addition, route-compression is also performed.

        Args:
            v (int): The index of the specified node.

        Returns:
            int: The index of the root.

        """

        # Return itself if node v is the root.
        if self._parent[v] == v:
            return v

        # Get the root recursively.
        r: int = self.root(self._parent[v])
        # Accumulate weight.
        self._diff_weight[v] += self._diff_weight[self._parent[v]]
        # Update the list.
        self._parent[v] = r

        # Return the root.
        return r

    def weight(self, v: int) -> T:
        """Returns the weight of the node.

        Returns the weight difference between the root and the node.

        Args:
            v (int): The index of the node.

        """
        # Conduct route-compression.
        self.root(v)

        # Return the difference of weight.
        return self._diff_weight[v]

    def is_same(self, x: int, y: int) -> bool:
        """Determine if they are in same group.

        Determine if they are in same group.

        Args:
            x (int): The index of the node.
            y (int): The index of the other node.

        Returns:
            bool: True if x and y are belonging same group. Otherwise, False.

        """
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int, w: T) -> bool:
        """Merge two nodes.

        Merge specified two nodes.

        Args:
            x (int): The index of the node.
            y (int): The index of the other node.
            w (T): The weight difference between x and y.

        Returns:
            bool: False if x and y are already in same group.

        """

        # Compensate the weight because each root is merged in fact.
        w += self.weight(x)
        w -= self.weight(y)

        # Move to each root.
        x = self.root(x)
        y = self.root(y)

        # Return false if x and y are already in same group.
        if x == y:
            return False

        # Swap so that the rank of x is higher.
        if self._rank[x] < self._rank[y]:
            x, y = y, x
            w = -w

        # If the two trees are the same rank, the rank increases by 1 after merge.
        if self._rank[x] == self._rank[y]:
            self._rank[x] += 1

        # Update parent.
        self._parent[y] = x

        # Update weight.
        self._diff_weight[y] = w

        # Successfully merged.
        return True

    def diff(self, x: int, y: int) -> T:
        return self.weight(y) - self.weight(x)


def main():
    N, Q = map(int, input().split())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    uf = WeightedUnionFind[int](N, 0)

    for q in query:
        if q[0] == 0:
            x, y, z = q[1:]

            uf.unite(x, y, z)

        else:
            x, y = q[1:]
            if uf.is_same(x, y):
                print(uf.diff(x, y))
            else:
                print("?")


if __name__ == "__main__":
    main()
