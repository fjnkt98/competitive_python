import sys

sys.setrecursionlimit(1000000)


def main() -> None:
    N: int = int(input())
    P: list[int] = [int(v.strip()) for v in input().split()]

    j = N - 2
    while P[j] < P[j + 1]:
        j -= 1

    k = N - 1
    while P[j] < P[k]:
        k -= 1

    P[j], P[k] = P[k], P[j]
    print(*P[: j + 1], *P[:j:-1])


if __name__ == "__main__":
    main()
