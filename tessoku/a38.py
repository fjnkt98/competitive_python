def main() -> None:
    D, N = map(int, input().split())
    if N == 0:
        print(24 * D)
        return
    L, R, H = map(
        list, zip(*[list(map(int, input().split())) for i in range(N)])
    )

    A = [24 for _ in range(D + 1)]
    A[0] = 0
    for l, r, h in zip(L, R, H):
        for i in range(l, r + 1):
            A[i] = min(A[i], h)

    print(sum(A))


if __name__ == "__main__":
    main()
