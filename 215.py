def main():
    N: int = int(input())
    A: list[int] = list(map(int, input().split()))

    answer: int = 0
    for i in range(1, N):
        if A[i] > A[i - 1]:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
