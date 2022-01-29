def main():
    N = int(input())
    A = list(map(int, input().split()))

    maximum: int = max(A)

    answer: int = -1
    for i, a in enumerate(A):
        if a == maximum:
            answer = i
            break

    print(answer)


if __name__ == "__main__":
    main()
