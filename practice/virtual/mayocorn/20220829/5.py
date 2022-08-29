from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))
    Q: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    table: Dict[int, int] = {
        **{a: random.randint(0, 1 << 60) for a in A},
        **{b: random.randint(0, 1 << 60) for b in B},
    }

    hash_a: List[int] = [0]
    set_a: Set[int] = set()
    for a in A:
        if a in set_a:
            hash_a.append(hash_a[-1])
        else:
            set_a.add(a)
            hash_a.append(hash_a[-1] ^ table[a])

    hash_b: List[int] = [0]
    set_b: Set[int] = set()
    for b in B:
        if b in set_b:
            hash_b.append(hash_b[-1])
        else:
            set_b.add(b)
            hash_b.append(hash_b[-1] ^ table[b])

    for x, y in zip(X, Y):
        print("Yes" if hash_a[x] == hash_b[y] else "No")


if __name__ == "__main__":
    main()
