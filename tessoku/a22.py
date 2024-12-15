def main() -> None:
    N: int = int(input())
    A: list[int] = [0] + [int(v.strip()) for v in input().split()]
    B: list[int] = [0] + [int(v.strip()) for v in input().split()]

    dp = [-int(1e9) for _ in range(N + 1)]
    dp[0] = 0
    dp[1] = 0

    for i in range(1, N):
        dp[A[i]] = max(dp[A[i]], dp[i] + 100)
        dp[B[i]] = max(dp[B[i]], dp[i] + 150)

    print(dp[N])


if __name__ == "__main__":
    main()
