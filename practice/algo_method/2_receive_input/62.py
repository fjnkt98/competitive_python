def main():
    N = int(input())
    S: list[str] = [input() for i in range(N)]

    left: int = 0
    right: int = 0
    for s in S:
        if s == "left":
            left += 1
        elif s == "right":
            right += 1

    if left == right:
        print("same")
    elif left > right:
        print("left")
    else:
        print("right")


if __name__ == "__main__":
    main()
