def main():
    N = int(input())

    count: int = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
