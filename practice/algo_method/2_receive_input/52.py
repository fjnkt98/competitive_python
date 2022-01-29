def main():
    N = int(input())
    A = list(map(int, input().split()))

    for a in A:
        print(a % 10)


if __name__ == "__main__":
    main()
