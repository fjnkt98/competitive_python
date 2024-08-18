def main() -> None:
    N: int = int(input())

    c = 0
    mod = 10000
    for t, a in [input().split() for _ in range(N)]:
        a = int(a)
        if t == "+":
            c += a
        elif t == "-":
            c -= a
            if c < 0:
                c += mod
        else:
            c *= a

        c %= mod
        print(c)


if __name__ == "__main__":
    main()
