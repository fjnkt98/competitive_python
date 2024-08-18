def main() -> None:
    N: int = int(input())
    A: list[int] = [0] * 1 + [int(v.strip()) for v in input().split()]
    B: list[int] = [0] * 2 + [int(v.strip()) for v in input().split()]

    P = [-1] * N

    dp = [1 << 60] * N
    dp[0] = 0
    dp[1] = A[1]
    P[0] = 0
    P[1] = 0

    for i in range(2, N):
        a = dp[i - 1] + A[i]
        b = dp[i - 2] + B[i]
        if a < b:
            dp[i] = a
            P[i] = i - 1
        else:
            dp[i] = b
            P[i] = i - 2

    c = N - 1
    R = [c]
    while c != 0:
        c = P[c]
        R.append(c)

    print(len(R))
    print(*map(lambda x: x + 1, reversed(R)))


if __name__ == "__main__":
    main()
