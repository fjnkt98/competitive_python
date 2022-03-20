from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(patties: List[int], layers: List[int], level: int, X: int) -> int:
    if level == 0:
        return 1

    if X < 1:
        return 0
    X -= 1

    if X < layers[level - 1]:
        return f(patties, layers, level - 1, X)
    X -= layers[level - 1]

    if X < 1:
        return patties[level - 1] + 1
    X -= 1

    if X < layers[level - 1]:
        return patties[level - 1] + 1 + f(patties, layers, level - 1, X)
    X -= layers[level - 1]

    return patties[level - 1] * 2 + 1


def main():
    N, X = map(int, input().split())
    X -= 1

    patties: List[int] = [0 for i in range(N + 1)]
    layers: List[int] = [0 for i in range(N + 1)]

    layers[0] = 1
    for i in range(1, N + 1):
        layers[i] = 2 * layers[i - 1] + 3

    patties[0] = 1
    for i in range(1, N + 1):
        patties[i] = 2 * patties[i - 1] + 1

    print(f(patties, layers, N, X))


if __name__ == "__main__":
    main()
