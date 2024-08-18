import bisect


def main() -> None:
    N, X = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]

    i = bisect.bisect_left(A, X)
    print(i + 1)


if __name__ == "__main__":
    main()
