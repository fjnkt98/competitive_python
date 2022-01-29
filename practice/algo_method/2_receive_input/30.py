def main():
    A, B = map(int, input().split())

    residueA = A % 10
    residueB = B % 10

    if residueA < residueB:
        print(A)
    else:
        print(B)


if __name__ == "__main__":
    main()
