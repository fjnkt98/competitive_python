from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    Q: int = int(input())
    query: List[List[int, int]] = [list(map(int, input().split())) for i in range(Q)]

    deck: Deque[int] = collections.deque()
    for t, x in query:
        if t == 1:
            deck.appendleft(x)
        elif t == 2:
            deck.append(x)
        elif t == 3:
            print(deck[x - 1])


if __name__ == "__main__":
    main()
