from typing import List
from math import trunc, sqrt


def enumerate_dividers(x: int) -> List[int]:
    result: List[int] = []

    for i in range(1, trunc(sqrt(x)) + 1):
        if x % i == 0:
            result.append(i)

            if x // i != i:
                result.append(x // i)

    result.sort()

    return result


def main():
    N, K = map(int, input().split())

    count: int = 0
    for i in range(1, N + 1):
        if len(enumerate_dividers(i)) == K:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
