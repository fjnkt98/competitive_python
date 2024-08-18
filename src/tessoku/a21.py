def main() -> None:
    N: int = int(input())
    P, A = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    P = [p - 1 for p in P]

    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for l in range(N - 1, 0, -1):
        for i in range(0, N - l + 1):
            j = i + l

            if i > 0:
                dp[i][j] = max(
                    dp[i][j], dp[i - 1][j] + (A[i - 1] if i <= P[i - 1] < j else 0)
                )
            if j < N:
                dp[i][j] = max(dp[i][j], dp[i][j + 1] + (A[j] if i <= P[j] < j else 0))

    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][i + 1])
    print(answer)


if __name__ == "__main__":
    main()
