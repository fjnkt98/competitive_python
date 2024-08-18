import bisect


def main() -> None:
    N: int = int(input())
    A: list[int] = [int(v.strip()) for v in input().split()]

    dp = [1 << 60 for _ in range(N)]
    for a in A:
        dp[bisect.bisect_left(dp, a)] = a

    print(bisect.bisect_left(dp, 1 << 60))


if __name__ == "__main__":
    main()
