from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    F: List[List[int, int]] = [list(map(int, input().split())) for i in range(N)]

    F.sort(key=lambda x: x[1])

    answer: int = 0
    endpoint: int = 0
    for s, t in F:
        if s < endpoint:
            continue
        else:
            endpoint = t
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
