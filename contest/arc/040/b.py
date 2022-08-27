from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N, R = map(int, input().split())
    S: List[str] = list(input())
    # N: int = random.randint(1, 100)
    # R: int = random.randint(1, N)
    # S = ["." if random.random() > 0.5 else "o" for i in range(N)]
    # print(N, R)
    # print("".join(S))

    last: int = "".join(S).rfind(".") - R + 1
    # print(last)

    X: int = 0
    answer: int = 0
    while X < N:
        if S[X] == ".":
            for i in range(X, min(X + R, N)):
                S[i] = "o"
            answer += 1
        else:
            if S.count("o") == N:
                break
            while S[X] == "o":
                if X >= last:
                    answer += 1
                    print(answer)
                    return

                X += 1
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()
