from typing import List, Tuple, Deque, Set, Dict, Callable, Generic, TypeVar
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


# Type of the element of segment tree
S = TypeVar("S")
# Type of the operator
F = TypeVar("F")


class LazySegmentTree(Generic[S, F]):
    """Segment Tree with Lazy Propagation

    Non-recursive, and abstracted lazy segment tree implementation.

    Attributes:
        -N (int): Number of the elements managed by segment tree.
        _op (Callable[[S, S], S]): A function object representing the binary operator.
        _e (Callable[[], int]): A function object which returns identity element.
        _mapping (Callable[[F, S], S]): A function object representing the mapping.
                                        mapping() takes the operator f and target
                                        element s,
                                        and returns the result.
        _composition (Callable[[F, F], F]): A function object representing the
                                            composition of maps.
                                            composition() takes two operator, and
                                            returns composited operator.
        _id (Callable[[], F]): A function object representing identity mapping.
        _log (int): The logarithm of size of segment tree base 2.
        _size (int): Size of the list that representing binary tree object.
        _data (List[S]): A list of the entities representing segment tree.(1-indexed)
        _lazy (List[F]): A list for lazy propagation. lazy[k] holds the operation
                         performed in the segment corresponding to the data[k] which
                         haven't yet been applied to the nodes below the data[k].

    """

    def __init__(
        self,
        op: Callable[[S, S], S],
        e: Callable[[], S],
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        id: Callable[[], F],
        A: List[S],
    ):
        """Constructor

        Construct segment tree

        Args:
            op (Callable[[S, S], S])
            e (Callable[[], S])
            mapping (Callable[[F, S], S])
            composition (Callable[[F, F], F])
            id (Callable[[], F])
            A (List[S])

        """

        self._N: int = len(A)
        self._op: Callable[[S, S], S] = op
        self._e: Callable[[], S] = e
        self._mapping: Callable[[F, S], S] = mapping
        self._composition: Callable[[F, F], F] = composition
        self._id: Callable[[], F] = id
        self._log: int = (self._N - 1).bit_length()
        self._size: int = 1 << self._log
        # Initialize each element of the list with identity element.
        self._data: List[S] = [self._e()] * (2 * self._size)
        self._lazy: List[F] = [self._id()] * self._size

        # Initialize leaves with given list A.
        self._data[self._size : self._size + self._N] = A

        # Update all nodes (not leaf).
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, k: int, x: S) -> None:
        """Set x into the specified leaf.

        Args:
            k (int): The index of the leaf(0-indexed).

        """

        # Move to the leaf.
        k += self._size

        # Propagate pending operator from the root to the leaf.
        for i in range(self._log, 0, -1):
            self._propagate(k >> i)

        # Update value of the element from the leaf to the root.
        for i in range(i, self._log + 1):
            self._update(k >> i)

    def get(self, k: int) -> S:
        """Get the value of the specified leaf.

        Args:
            k (int): The index of the leaf(0-indexed).

        Returns:
            S: Value of the specified leaf.

        """

        # Move to the leaf.
        k += self._size

        # Propagate pending operator from the root to the leaf.
        for i in range(self._log, 0, -1):
            self._propagate(k >> i)

        # Return the value.
        return self._data[k]

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

        # Propagate pending operator from the root to the leaf
        # for calculate the production
        for i in range(self._log, 0, -1):
            # In the subtree containing the l, when the l is the leftmost node,
            # don't have to propagate. Because the root of the subtree has all
            # information of l.
            if ((l >> i) << i) != l:
                self._propagate(l >> i)
            # Same to above.
            if ((r >> i) << i) != r:
                self._propagate((r - 1) >> i)

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

    def apply(self, k: int, f: F) -> None:
        """Apply the mapping to single leaf.

        Apply the mapping to the single leaf with specified index.

        Args:
            k (int): Index of the leaf(0-indexed).
            f (F): The value to be acted on the leaf.

        """

        # Move to leaf.
        k += self._size

        # Propagate pending operator from the root to the leaf.
        for i in range(self._log, 0, -1):
            self._propagate(k >> i)

        # Apply the mapping to the leaf.
        self._data[k] = self._mapping(f, self._data[k])

        # Update ancestors.
        for i in range(1, self._log + 1):
            self._update(k >> i)

    def apply_each(self, l: int, r: int, f: F) -> None:
        """Apply the mapping to each leaves of the specified interval.

        Apply the mapping to each leaves of the specified interval [l, r).

        Args:
            l (int): Left end of the given interval.
            r (int): Right end of the given interval.
            f (F): The value to be acted on the leaves.

        """

        # When invalid interval was given
        if l >= r:
            return

        # Move to child.
        l += self._size
        r += self._size

        # Propagate pending operator from the root to the leaf
        # for calculate the production
        for i in range(self._log, 0, -1):
            # In the subtree containing the l, when the l is the leftmost node,
            # don't have to propagate. Because the root of the subtree has all
            # information of l.
            if ((l >> i) << i) != l:
                self._propagate(l >> i)
            # Same to above.
            if ((r >> i) << i) != r:
                self._propagate((r - 1) >> i)

        # Copy the variable for temporary calculation.
        left: int = l
        right: int = r
        # Find all nodes covering the given interval, and apply the mapping to them.
        while left < right:
            # If left is right child
            if left & 1:
                # Apply the mapping.
                self._reflect(left, f)
                # Move to elder brother.
                left += 1

            # If right is right child
            if right & 1:
                # Move to little brother.
                right -= 1
                # Apply the mapping.
                self._reflect(right, f)

            # Move to parent.
            left >>= 1
            right >>= 1

        # Update value of the ancestors.
        for i in range(1, self._log + 1):
            # In the subtree containing the l, when the l is the leftmost node,
            # don't have to update. Because the root of the subtree has all
            # information of l.
            if ((l >> i) << i) != l:
                self._update(l >> i)
            # Same to above.
            if ((r >> i) << i) != r:
                self._update(r >> i)

    def _reflect(self, k: int, f: F) -> None:
        """Recleft the operation on the node.

        Reflect the specified operator f on the node data[k], and if the node is leaf,
        combine the operator f with lazy[k].

        Args:
            k (int): The index of the node (0-indexed).
            f (F): The operator.

        """

        # Reflect the operator on the node.
        self._data[k] = self._mapping(f, self._data[k])

        # When k is not leaf
        if k < self._size:
            # Combine the operator f with lazy[k]
            self._lazy[k] = self._composition(f, self._lazy[k])

    def _propagate(self, k: int) -> None:
        """Propagate pending operator to each child.

        Propagate pending operator lazy[k] to each child, and reset lazy[k].


        Args:
            k (int): The index of the node (0-indexed).

        """

        # Propagate operator lazy[k] to left child.
        self._reflect(2 * k, self._lazy[k])
        # Propagate operator lazy[k] to right child.
        self._reflect(2 * k + 1, self._lazy[k])

        # Reset lazy[k]
        self._lazy[k] = self._id()

    def _update(self, k: int) -> None:
        """Update the element.

        Update value of the element with the value of the child node.

        Args:
            k (int): The index of the node (0-indexed).

        """
        self._data[k] = self._op(self._data[2 * k], self._data[2 * k + 1])


def main():
    W, N = map(int, input().split())
    bricks: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(N)]

    seg = LazySegmentTree[int, int](
        lambda x, y: max(x, y),
        lambda: -(1 << 60),
        lambda f, s: s if f == -1 else f,
        lambda f, g: g if f == -1 else f,
        lambda: -1,
        [0 for i in range(W)],
    )

    answer: List[int] = [0] * N
    for i, (L, R) in enumerate(bricks):
        height: int = seg.prod(L - 1, R)
        seg.apply_each(L - 1, R, height + 1)
        answer[i] = seg.prod(L - 1, R)

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
