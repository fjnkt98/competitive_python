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


T = TypeVar("T", int, Tuple)


class SortedSet(Generic[T]):
    """Implementation of sorted set by square-root decomposition.

    This class was implemented by refering to the following URL:
    https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py

    A (List[List[T]]): A list of list retaining the elements of the set.
    size (int): The size of the set.
    BUCKET_RATIO (int): The ratio of the number of buckets to the number of elements
    in each bucket.
    REBUILD_RATIO (int): Threshold for the ratio of buckets to rebuild.

    """

    def __init__(self, a: Iterable[T] = []) -> None:
        """Create new sorted set from iterable.

        Args:
            a (Iterable[T]): The source for building sorted set.
        """
        # Convert to list
        a = list(a)
        # When a is not sorted or unique, do so.
        if not all(i < j for i, j in zip(a[0:-1], a[1:])):
            a = sorted(set(a))

        # Configure threshold of ratio
        self.BUCKET_RATIO: int = 50
        self.REBUILD_RATIO: int = 170

        # Calculate and store length of sorted set.
        self.size: int = len(a)
        # Build the sorted set.
        self._build(a)

    def _build(self, a: Iterable[T] = None) -> None:
        """Evenly divide the container into buckets.

        Args:
            a (Iterable[T]): The source for building sorted set.
        """
        # When the iterable was given, use it and override the container.
        # Convert the given iterable into list.
        if a is None:
            a = list(self)
        else:
            a = list(a)

        # Calculate length of the iterable.
        size: int = len(a)
        # Calculate each bucket size.
        bucket_size: int = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        # Divide the source into buckets.
        self.A: List[List[T]] = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.A:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.A):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.A)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        """Find the bucket which should contain x.

        Args:
            x (T): The element of the set for search.

        Return:
            List[T]: The bucket which is containing x.
        """
        for a in self.A:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False

        a = self._find_bucket(x)
        i = bisect.bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        """Add an element into the set.

        Args:
            x (T): The element to add.

        Return:
            bool: True if the element was added, or False.
        """
        # WHen the set is empty:
        if self.size == 0:
            self.A = [[x]]
            self.size = 1
            return True

        # Get the bucket in which x should be.
        a = self._find_bucket(x)
        # Get the index at which x should be inserted.
        i = bisect.bisect_left(a, x)
        # WHen  x is already exist in the set
        if i != len(a) and a[i] == x:
            return False

        # Add x into the bucket.
        a.insert(i, x)
        # Increase size of the set.
        self.size += 1
        # When the ratio exceed the threshold, rebuild the set
        if len(a) > len(self.A) * self.REBUILD_RATIO:
            self._build()

        return True

    def discard(self, x: T) -> bool:
        """Remove an element from the set.

        Args:
            x (T): The element to remove.

        Return:
            bool: True if the element was successfully removed.
        """
        # When the set is empty:
        if self.size == 0:
            return False

        # Get the bucket which is containing x.
        a = self._find_bucket(x)
        # Get the index of x.
        i = bisect.bisect_left(a, x)

        # When the bucket doesn't have x:
        if i == len(a) or a[i] != x:
            return False

        # Remove x.
        a.pop(i)
        # Decrease size of the set.
        self.size -= 1
        # If the bucket become empty, rebuild the container.
        if len(a) == 0:
            self._build()

        return True

    def lt(self, x: T) -> Union[T, None]:
        """Find the largest element less than x.

        Args:
            x (T): The element for search.

        Return:
            T: The largest element less than x.
            If it doesn't exist, return None.
        """
        for a in reversed(self.A):
            if a[0] < x:
                return a[bisect.bisect_left(a, x) - 1]
        return None

    def le(self, x: T) -> Union[T, None]:
        """Find the largest element less than or equal to  x.

        Args:
            x (T): The element for search.

        Return:
            T: The largest element less than or equal to  x.
            If it doesn't exist, return None.
        """
        for a in reversed(self.A):
            if a[0] <= x:
                return a[bisect.bisect_left(a, x) - 1]
        return None

    def gt(self, x: T) -> Union[T, None]:
        """Find the smallest element greater than x.

        Args:
            x (T): The element for search.

        Return:
            T: The smallest element greater than x.
            If it doesn't exist, return None.
        """
        for a in self.A:
            if a[-1] > x:
                return a[bisect.bisect_right(a, x)]
        return None

    def ge(self, x: T) -> Union[T, None]:
        """Find the smallest element greater than or equal to  x.

        Args:
            x (T): The element for search.

        Return:
            T: The smallest element greater than or equal to  x.
            If it doesn't exist, return None.
        """
        for a in self.A:
            if a[-1] >= x:
                return a[bisect.bisect_right(a, x)]

        return None

    def __getitem__(self, x: int) -> T:
        """Return the x-th element in the set.

        Raise IndexError when it doesn't exist.

        """
        if x < 0:
            x += self.size

        if x < 0:
            raise IndexError

        for a in self.A:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        """Count the number of elements which is less than x.

        Args:
            x (T): The element fot search.

        Return:
            int: The number of elements which is less than x.
        """
        result: int = 0
        for a in self.A:
            if a[-1] >= x:
                return result + bisect.bisect_left(a, x)
            result += len(a)

        return result

    def index_right(self, x: T) -> int:
        """Count the number of elements which is greater than or equal to x.

        Args:
            x (T): The element fot search.

        Return:
            int: The number of elements which is greater than or equal to x.
        """
        result: int = 0
        for a in self.A:
            if a[-1] > x:
                return result + bisect.bisect_right(a, x)
            result += len(a)

        return result


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
    N, K = map(int, input().split())
    P: List[int] = list(map(int, input().split()))

    answer: List[int] = [-1] * (N + 1)

    S = SortedSet()
    uf = UnionFind(N + 1)

    for i, p in enumerate(P):
        index: int = S.index_right(p)
        if len(S) == 0 or index == len(S):
            S.add(p)
        elif S[index] < p:
            S.add(p)
        else:
            uf.unite(p, S[index])
            S.discard(S[index])
            S.add(p)

        if uf.get_size(p) == K:
            answer[uf.get_root(p)] = i + 1
            S.discard(p)

    for i in range(1, N + 1):
        answer[i] = answer[uf.get_root(i)]

    for a in answer[1:]:
        print(a)


if __name__ == "__main__":
    main()
