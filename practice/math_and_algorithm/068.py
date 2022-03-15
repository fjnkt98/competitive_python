from typing import List, Tuple, Set
import sys
from array import array
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    V: List[int] = list(map(int, input().split()))

    answer: int = 0
    for bits in itertools.product([0, 1], repeat=K):
        lcm: int = 1
        for bit, v in zip(bits, V):
            if bit == 1:
                lcm = lcm * v // math.gcd(lcm, v)

        if sum(bits) % 2 == 0:
            answer += N // lcm
        else:
            answer -= N // lcm

    print(N - answer)


if __name__ == "__main__":
    main()
