def main():
    N = int(input())
    A = list(map(int, input().split()))

    answer: int = 0
    for a in A:
        if a > 0:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
