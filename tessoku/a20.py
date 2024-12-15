def main() -> None:
    S: str = input().rstrip()
    T: str = input().rstrip()

    N = len(S)
    M = len(T)

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i, s in enumerate(S, 1):
        for j, t in enumerate(T, 1):
            if s == t:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[N][M])


if __name__ == "__main__":
    main()
