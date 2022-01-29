def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = sum(A)

    print(S // N)


if __name__ == "__main__":
    main()
