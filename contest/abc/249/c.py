from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def encode(c: str) -> int:
    return ord(c) - ord("a")


def main():
    N, K = map(int, input().split())
    S: List[str] = [input() for i in range(N)]

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=N):
        T: List[str] = []
        for i, bit in enumerate(bits):
            if bit == 1:
                T.append(S[i])

        count: List[int] = [0] * 26
        for t in T:
            for c in t:
                count[encode(c)] += 1

        various: int = 0
        for c in count:
            if c == K:
                various += 1

        answer = max(answer, various)

    print(answer)


if __name__ == "__main__":
    main()
