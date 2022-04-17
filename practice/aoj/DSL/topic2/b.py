from typing import List, Tuple, Callable
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


class SegmentTree:
    """Segment Tree

    Non-recursive, and abstracted segment tree implementation(not lazy evaluation).
    You can only use integer as segment tree elements.

    Attributes:
        _N (int): Length of target list.
        _op (Callable[[int, int], int]): A function object representing the binary
                                         operator.
        _e (Callable[[], int]): A function object representing identity element.
        _size (int): Size of the list that representing binary tree object.
        _data (List[int]): A List of the entity representing segment tree.(1-indexed)

    """

    def __init__(
        self,
        op: Callable[[int, int], int],
        e: Callable[[], int],
        N: int,
        A: List[int] = None,
    ):
        """Constructor

        Construct segment tree

        Args:
            op (Callable[[int, int], int]): A function object represent the binary
                                            operator.
            e (Callable[[], int]): A function object representing identity element.
            N (int): Length of target list.
            A (List[int]): (Optional) The target list.

        """

        self._N: int = N
        self._op: Callable[[int, int], int] = op
        self._e: Callable[[], int] = e
        # Minimum power of 2 which is greater than or equal to  N
        self._size: int = 1 << ((N - 1).bit_length())
        # Initialize each element of the list with identity element
        self._data: List[int] = [self._e()] * (2 * self._size)

        # When target list is given, assign and initialize leaves and nodes of
        # segment tree with its elements
        if A is not None:
            for i, a in enumerate(A):
                self._data[i + self._size] = a

            for i in range(self._size - 1, 0, -1):
                self._data[i] = self._op(self._data[2 * i], self._data[2 * i + 1])

    def update(self, k: int, x: int) -> None:
        """Update element

        Update value of specified leaf and calculate each nodes which contains
        specified leaf

        Args:
            k (int): Index of target leaf (0-indexed)
            x (int): The value

        """

        # Move to the leaf
        k += self._size

        # Update value of the leaf
        self._data[k] = x
        # Update related nodes
        while k > 1:
            # Move to parent
            k >>= 1
            # Update value of node
            self._data[k] = self._op(self._data[2 * k], self._data[2 * k + 1])

    def find(self, l: int, r: int) -> int:
        """Get the value corresponding to a given segment

        Get the value corresponding to a given segment [l, r) (0-indexed).

        Args:
            l (int): Index indicating left end of the segment.
            r (int): Index indicating right end of the segment.

        Returns:
            int: The value corresponding to a given segment.

        """

        # Result of left side
        left_result: int = self._e()
        # Result of right side
        right_result: int = self._e()

        # Move to leaf
        l += self._size
        r += self._size

        # Until there are no more not calculated segment
        while l < r:
            # when l is left child
            if l & 1:
                left_result = self._op(left_result, self._data[l])
                l += 1

            # when r is right child
            if r & 1:
                r -= 1
                right_result = self._op(right_result, self._data[r])

            # Move to parent
            l >>= 1
            r >>= 1

        # Return the result
        return self._op(left_result, right_result)

    def get_root(self) -> int:
        """Get the value of the entire segment

        Get the value of the entire segment.

        """

        return self._data[1]

    def get(self, i: int) -> int:
        """Get the value of specified leaf

        Get the value of specified leaf.


        Args:
            i (int): Index of the leaf(0-indexed).

        Returns:
            int: Value of the specified leaf.

        """

        return self._data[i + self._size]


def main():
    N, Q = map(int, input().split())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    seg = SegmentTree(lambda x, y: x + y, lambda: 0, N)

    for t, x, y in query:
        if t == 0:
            seg.update(x - 1, seg.get(x - 1) + y)
        else:
            print(seg.find(x - 1, y))


if __name__ == "__main__":
    main()
