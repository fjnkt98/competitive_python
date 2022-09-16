from typing import *
import collections
import itertools
import bisect
import math


# Type of the element of segment tree
S = TypeVar("S")


class SegmentTree(Generic[S]):
    """Segment Tree

    Non-recursive, and abstracted segment tree implementation.

    Attributes:
        -N (int): Number of the elements managed by segment tree.
        _op (Callable[[S, S], S]): A function object representing the binary operator.
        _e (Callable[[], int]): A function object which returns identity element.
        _log (int): The logarithm of size of segment tree base 2.
                    Also this represent the height of the tree.
        _size (int): Number of the leaves of the tree
        _data (List[S]): A list of the entities representing segment tree.(1-indexed)

    """

    def __init__(self, op: Callable[[S, S], S], e: Callable[[], S], A: List[S]):
        """Constructor

        Args:
            op (Callable[[S, S], S]): A function representing the binary operator.
            e (Callable[[], S]): A function representing identity element.
            A (List[S]): A list containing the initial values of leaves.
        """
        self._N = len(A)
        self._op = op
        self._e = e
        # Calculate tree size.
        self._log: int = (self._N - 1).bit_length()
        self._size: int = 1 << self._log
        # Segment tree is represented by a list of length 2N
        # because it's a full binary tree.
        self._data: List[S] = [self._e()] * (2 * self._size)

        # Initialize leaves with given list A.
        self._data[self._size : self._size + self._N] = A

        # Update all non-leaf nodes.
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def __setitem__(self, key: int, value: S) -> None:
        """Point Update: Set the value into the specified leaf.

        Args:
            key (int): The index of the leaf (0-indexed).
            value (S): The value to apply.
        """

        # Type check
        if not isinstance(key, int):
            raise TypeError

        # Move to the leaf.
        key += self._size

        # Set the value of the leaf
        self._data[key] = value

        # Update value of the element from the leaf to the root.
        for i in range(1, self._log + 1):
            self._update(key >> i)

    def __getitem__(self, key: Union[int, slice]) -> S:
        """Point Acquisition: Get the production of the specified point of interval.

        Args:
            key (int or slice): The index of the leaf, or interval (0-indexed).
            if key is int, return the value of the leaf.
            if key is slice, return the product of the interval.

        Return:
            S: The product.
        """
        # Type check
        if isinstance(key, int):
            # When key is int, return the value of the leaf.
            return self._data[key + self._size]
        elif isinstance(key, slice):
            # Value check
            l: int = 0 if key.start is None else key.start
            r: int = self._N if key.stop is None else key.stop

            if not (0 <= l < self._size and 0 <= r <= self._size):
                raise IndexError

            # WHen key is slice, return the value of the leaf

            return self.prod(l, r)

        else:
            raise TypeError

    def prod(self, l: int, r: int) -> S:
        """Returns op(A[l], ..., A[r - 1]).

        Returns the product of the interval [l, r).

        Args:
            l (int): Left end of the given interval.
            r (int): Right end of the given interval. it doesn't include
                     the right end.

        Return:
            S: The product.
        """

        # When invalid interval was given
        if l >= r:
            return self._e()

        # Move to leaf
        l += self._size
        r += self._size

        # Variable to hold the left result
        left_result: S = self._e()
        # Variable to hold the right result
        right_result: S = self._e()

        # Find all nodes covering the given interval.
        while l < r:
            # If l is right child
            if l & 1:
                # Calculate result.
                left_result = self._op(left_result, self._data[l])
                # Move to elder sibling.
                l += 1

            # If r is right child
            if r & 1:
                # Move to little sibling.
                r -= 1
                # Calculate result.
                right_result = self._op(right_result, self._data[r])

            # Move to parent.
            l >>= 1
            r >>= 1

        # Return the result.
        return self._op(left_result, right_result)

    def _update(self, k: int) -> None:
        """Update the element.

        Update value of the element with the value of the child node.

        Args:
            k (int): The index of the node (0-indexed).

        """
        self._data[k] = self._op(self._data[2 * k], self._data[2 * k + 1])

    def __len__(self) -> int:
        """Return the size of tree."""
        return 2 * self._size

    def __iter__(self) -> Iterator[S]:
        """Return the leaves iterator corresponding to A"""
        for d in self._data[self._size : self._size + self._N]:
            yield d


def main():
    N, M = map(int, input().split())
    D: List[int] = [0] + [int(input()) for i in range(N)]
    C: List[int] = [0] + [int(input()) for i in range(M)]

    dp: List[List[int]] = [[1 << 60 for j in range(M + 1)] for i in range(N + 1)]
    dp[0] = [c * D[0] for c in C]

    seg = SegmentTree[int](lambda a, b: min(a, b), lambda: 1 << 60, dp[0])
    for i in range(1, N + 1):
        for j in range(i, M + 1):
            dp[i][j] = seg[0:j] + D[i] * C[j]
        seg = SegmentTree[int](lambda a, b: min(a, b), lambda: 1 << 60, dp[i])

    print(min(dp[N]))


if __name__ == "__main__":
    main()
