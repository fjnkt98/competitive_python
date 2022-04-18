from typing import List, Tuple, Generic, TypeVar, Callable
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


S = TypeVar("S")
F = TypeVar("F")


class LazySegmentTree(Generic[S, F]):
    def __init__(
        self,
        op: Callable[[S, S], S],
        e: Callable[[], S],
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        id: Callable[[], F],
        A: List[S],
    ):
        self._N: int = len(A)
        self._op: Callable[[S, S], S] = op
        self._e: Callable[[], S] = e
        self._mapping: Callable[[F, S], S] = mapping
        self._composition: Callable[[F, F], F] = composition
        self._id: Callable[[], F] = id
        self._log: int = (self._N - 1).bit_length()
        self._size: int = 1 << self._log
        self._data: List[S] = [self._e()] * (2 * self._size)
        self._lazy: List[F] = [self._id()] * self._size

        for i, a in enumerate(A):
            self._data[i + self._size] = a

        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, k: int, x: S) -> None:
        k += self._size

        for i in range(self._log, 0, -1):
            self._propagate(k >> i)

        self._data[k] = x

        for i in range(1, self._log + 1):
            self._update(k >> i)

    def get(self, k: int) -> S:
        k += self._size
        for i in range(self._log, 0, -1):
            self._propagate(k >> i)

        return self._data[k]

    def prod(self, l: int, r: int) -> S:
        if l >= r:
            return self._e()

        left_result: S = self._e()
        right_result: S = self._e()

        l += self._size
        r += self._size

        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._propagate(l >> i)
            if ((r >> i) << i) != r:
                self._propagate((r - 1) >> i)

        while l < r:
            if l & 1:
                left_result = self._op(left_result, self._data[l])
                l += 1

            if r & 1:
                r -= 1
                right_result = self._op(right_result, self._data[r])

            l >>= 1
            r >>= 1

        return self._op(left_result, right_result)

    def prod_all(self) -> S:
        return self._data[1]

    def apply(self, f: F, l: int, r: int = None) -> None:
        if r is None:
            l += self._size
            for i in range(self._log, 0, -1):
                self._propagate(l >> i)

            self._data[l] = self._mapping(f, self._data[l])

            for i in range(1, self._log + 1):
                self._update(l >> i)
        else:
            if l >= r:
                return

            l += self._size
            r += self._size

            for i in range(self._log, 0, -1):
                if ((l >> i) << i) != l:
                    self._propagate(l >> i)
                if ((r >> i) << i) != r:
                    self._propagate((r - 1) >> i)

            left: int = l
            right: int = r
            while left < right:
                if left & 1:
                    self._apply_all(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._apply_all(right, f)

                left >>= 1
                right >>= 1

            for i in range(1, self._log + 1):
                if ((l >> i) << i) != l:
                    self._update(l >> i)
                if ((r >> i) << i) != r:
                    self._update(r >> i)

    def _apply_all(self, k: int, f: F) -> None:
        self._data[k] = self._mapping(f, self._data[k])
        if k < self._size:
            self._lazy[k] = self._composition(f, self._lazy[k])

    def _propagate(self, k: int) -> None:
        self._apply_all(2 * k, self._lazy[k])
        self._apply_all(2 * k + 1, self._lazy[k])

        self._lazy[k] = self._id()

    def _update(self, k: int) -> None:
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
        seg.apply(height + 1, L - 1, R)
        answer[i] = seg.prod(L - 1, R)

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
