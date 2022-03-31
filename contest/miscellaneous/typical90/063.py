from typing import List, Tuple
import sys
import collections
import itertools
import copy


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=H):
        Q: List[List[int]] = []

        for i, bit in enumerate(bits):
            if bit == 1:
                Q.append(copy.copy(P[i]))

        if not Q:
            continue

        R: List[int] = []
        for j in range(W):
            same: bool = True
            for i, q in enumerate(Q):
                if q[j] != Q[0][j]:
                    same = False

            if same:
                R.append(Q[0][j])

        if not R:
            continue

        answer = max(answer, sum(bits) * collections.Counter(R).most_common(1)[0][1])

    print(answer)


if __name__ == "__main__":
    main()
