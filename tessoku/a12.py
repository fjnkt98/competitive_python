def main() -> None:
    N, K = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]

    left = 0
    right = 1 << 60
    while right - left > 1:
        mid = (left + right) // 2

        count = 0
        for a in A:
            count += mid // a

        if count < K:
            left = mid
        else:
            right = mid

    print(right)


if __name__ == "__main__":
    main()
