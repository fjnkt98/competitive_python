def main():
    N = int(input())
    A = list(map(int, input().split()))

    count: list[int] = [0 for i in range(9)]

    for a in A:
        count[a - 1] += 1

    maximum: int = max(count)
    for i, c in enumerate(count):
        if c == maximum:
            print(i + 1)
            break


if __name__ == "__main__":
    main()
