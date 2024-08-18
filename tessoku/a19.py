import itertools


def main() -> None:
    N, X = map(int, input().split())
    W, V = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    W = [0] + W
    V = [0] + V

    dp = [[0 for j in range(X + 1)] for i in range(N + 1)]
    for i, j in itertools.product(range(1, N + 1), range(X + 1)):
        dp[i][j] = dp[i - 1][j]

        if j - W[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i])

    print(dp[N][X])


if __name__ == "__main__":
    main()
