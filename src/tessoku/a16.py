def main() -> None:
    N: int = int(input())
    A: list[int] = [0] * 1 + [int(v.strip()) for v in input().split()]
    B: list[int] = [0] * 2 + [int(v.strip()) for v in input().split()]

    dp = [1 << 60] * N
    dp[0] = 0
    dp[1] = A[1]

    for i in range(2, N):
        dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

    print(dp[-1])


if __name__ == "__main__":
    main()
