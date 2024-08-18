def main() -> None:
    N, Q = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    dp = [[0 for _ in range(N + 1)] for _ in range(32)]
    for j, a in enumerate(A, start=1):
        dp[0][j] = a

    for i in range(1, 32):
        for j in range(1, N + 1):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    for x, y in zip(X, Y):
        answer = x
        i = 0
        while y:
            if y & 1:
                answer = dp[i][answer]
            y >>= 1
            i += 1
        print(answer)


if __name__ == "__main__":
    main()
