from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    Q: int = int(input())
    query: List[List[str]] = [input().rstrip().split() for i in range(Q)]

    pipe: Deque[Tuple[int, int]] = collections.deque()
    for s in query:
        if s[0] == "1":
            t, x, c = map(int, s)
            pipe.append((x, c))
        else:
            t, c = map(int, s)
            total: int = 0

            while pipe[0][1] < int(c):
                head: Tuple[int, int] = pipe.popleft()
                total += head[0] * head[1]
                c -= head[1]

            if c != 0:
                head: Tuple[int, int] = pipe.popleft()
                total += c * head[0]
                pipe.appendleft((head[0], head[1] - c))
                c = 0

            print(total)


if __name__ == "__main__":
    main()
