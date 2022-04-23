from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [input() for i in range(H)]

    count = collections.Counter(itertools.chain(*A))

    if H % 2 == 0 and W % 2 == 0:
        g1: int = 0
        g2: int = 0
        g4: int = (H // 2) * (W // 2)
    elif H % 2 == 1 and W % 2 == 1:
        g1: int = 1
        g2: int = H // 2 + W // 2
        g4: int = (H // 2) * (W // 2)
    else:
        g1: int = 0
        g2: int = W // 2 if W % 2 == 0 else H // 2
        g4: int = ((H - 1) // 2) * (W // 2) if W % 2 == 0 else (H // 2) * ((W - 1) // 2)

    for i in range(g1):
        for key, value in count.items():
            if value % 4 == 1 or value % 4 == 3:
                count[key] -= 1
                break

    for i in range(g2):
        for key, value in count.items():
            if value % 4 == 2:
                count[key] -= 2
                break

    for i in range(g4):
        for key, value in count.items():
            if value != 0 and value % 4 == 0:
                count[key] -= 4
                break

    if all(map(lambda x: x % 4 == 0, count.values())):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
