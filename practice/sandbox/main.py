from typing import List, Tuple, Deque, Set, Dict, Callable, Generic, TypeVar
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


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
        _size (int): Size of the list that representing binary tree object.
        _data (List[S]): A list of the entities representing segment tree.(1-indexed)

    """

    def __init__(self, op: Callable[[S, S], S], e: Callable[[], S], A: List[S]):
        self._N = len(A)
        self._op = op
        self._e = e
        self._log: int = (self._N - 1).bit_length()
        self._size: int = 1 << self._log
        self._data: List[S] = [self._e()] * (2 * self._size)

        # Initialize leaves with given list A.
        self._data[self._size : self._size + self._N] = A

        # Update all nodes (not leaf).
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def get(self, k: int) -> S:
        """Get the value of the specified leaf.

        Args:
            k (int): The index of the leaf(0-indexed).

        Returns:
            S: Value of the specified leaf.

        """

        return self._data[k + self._size]

    def set(self, k: int, x: S) -> None:
        """Set x into the specified leaf.

        Args:
            k (int): The index of the leaf(0-indexed).

        """

        # Move to the leaf.
        k += self._size

        # Set the value of the leaf
        self._data[k] = x

        # Update value of the element from the leaf to the root.
        for i in range(1, self._log + 1):
            self._update(k >> i)

    def prod(self, l: int, r: int) -> S:
        """Returns op(A[l], ..., A[r - 1]).

        Returns the result of applying the binary operator to the interval [l, r).

        Args:
            l (int): Left end of the given interval.
            r (int): Right end of the given interval. it doesn't not include
                     the right end.

        Returns:
            S: The result.

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
                # Move to elder brother.
                l += 1

            # If r is right child
            if r & 1:
                # Move to little brother.
                r -= 1
                # Calculate result.
                right_result = self._op(right_result, self._data[r])

            # Move to parent.
            l >>= 1
            r >>= 1

        # Return the result.
        return self._op(left_result, right_result)

    def prod_all(self) -> S:
        """Returns op(A[0], ..., A[N - 1]).

        Return the result of applying the binary operator to all monoids.

        Returns:
            S: The operation result.

        """
        return self._data[1]

    def _update(self, k: int) -> None:
        """Update the element.

        Update value of the element with the value of the child node.

        Args:
            k (int): The index of the node (0-indexed).

        """
        self._data[k] = self._op(self._data[2 * k], self._data[2 * k + 1])


def main():
    N, Q = map(int, input().split())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    seg = SegmentTree[int](
        lambda x, y: min(x, y), lambda: 1 << 60, [(1 << 31) - 1 for i in range(N)]
    )

    for q in query:
        if q[0] == 0:
            i, x = q[1:]
            seg.set(i, x)
        else:
            s, t = q[1:]
            print(seg.prod(s, t + 1))


if __name__ == "__main__":
    main()
