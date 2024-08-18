def main() -> None:
    N, M = map(int, input().split())
    A: list[list[int]] = [[int(v.strip()) for v in input().split()] for i in range(M)]
    B = [int("".join(map(str, A[i])), 2) for i in range(M)]

    dp = [[1 << 60 for j in range(1 << N)] for i in range(M + 1)]
    dp[0][0] = 0

    for i in range(M):
        for j in range(1 << N):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            dp[i + 1][j | B[i]] = min(dp[i + 1][j | B[i]], dp[i][j] + 1)

    print(-1 if dp[M][-1] == 1 << 60 else dp[M][-1])


if __name__ == "__main__":
    main()
