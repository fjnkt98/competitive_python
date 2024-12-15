import itertools


def main() -> None:
    N, S = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]

    dp = [[j == 0 for j in range(S + 1)] for _ in range(N + 1)]
    for i, j in itertools.product(range(1, N + 1), range(S + 1)):
        dp[i][j] |= dp[i - 1][j]
        if j - A[i - 1] >= 0:
            dp[i][j] |= dp[i - 1][j - A[i - 1]]

    if dp[N][S]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
