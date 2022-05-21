from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    reels: List[str] = [input() for i in range(N)]

    answer: int = 1 << 60
    for roll in range(10):
        times: List[int] = [0 for i in range(N)]

        for t, reel in enumerate(zip(*reels)):
            for i, r in enumerate(reel):
                if int(r) == roll:
                    times[i] = t

        stamp: Set[int] = set()
        for t in times:
            while True:
                if t in stamp:
                    t += 10
                else:
                    stamp.add(t)
                    break

        answer = min(answer, max(list(stamp)))

    print(answer)


if __name__ == "__main__":
    main()
