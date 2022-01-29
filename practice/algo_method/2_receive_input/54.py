def main():
    N = int(input())
    A = list(map(int, input().split()))

    answer: int = 1
    for a in A:
        answer *= a

    print(answer)


if __name__ == "__main__":
    main()
