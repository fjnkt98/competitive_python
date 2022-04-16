from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


class SegmentTreeRMQ:
    def __init__(self, N: int):
        M: int = 1
        while M * 2 <= N:
            M *= 2

        self.N: int = 2 * M
        self._data: List[int] = [(1 << 31) - 1] * (2 * self.N - 1)

    def update(self, k: int, a: int) -> None:
        k += self.N - 1
        self._data[k] = a
        while k > 0:
            k = (k - 1) // 2
            self._data[k] = min(self._data[2 * k + 1], self._data[2 * k + 2])

    def find(self, a: int, b: int, k: int, l: int, r: int) -> int:
        if r <= a or b <= l:
            return (1 << 31) - 1

        if a <= l and r <= b:
            return self._data[k]

        return min(
            self.find(a, b, 2 * k + 1, l, (l + r) // 2),
            self.find(a, b, 2 * k + 2, (l + r) // 2, r),
        )


def main():
    N, Q = map(int, input().split())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    st = SegmentTreeRMQ(N)
    for com, x, y in query:
        if com == 0:
            st.update(x, y)
        else:
            print(st.find(x, y + 1, 0, 0, st.N))


if __name__ == "__main__":
    main()
