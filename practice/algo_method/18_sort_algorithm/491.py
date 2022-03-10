from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    meals: List[List[int, int]] = [list(map(int, input().split())) for i in range(N)]

    meals.sort(key=lambda x: x[0])
    answer: int = 0
    for a, b in meals:
        if K - b < 0:
            answer += a * K
            K = 0
        else:
            answer += a * b
            K -= b

        if K <= 0:
            break

    print(answer)


if __name__ == "__main__":
    main()
