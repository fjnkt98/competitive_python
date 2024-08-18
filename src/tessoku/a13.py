import bisect


def main() -> None:
    N, K = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]

    count = 0
    for i, a in enumerate(A):
        j = bisect.bisect_right(A, a + K)
        count += j - i - 1

    print(count)


if __name__ == "__main__":
    main()
