def main() -> None:
    N, K = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]
    B: list[int] = [int(v.strip()) for v in input().split()]
    C: list[int] = [int(v.strip()) for v in input().split()]
    D: list[int] = [int(v.strip()) for v in input().split()]

    AB = [a + b for a in A for b in B]
    CD = set(c + d for c in C for d in D)

    ok = False
    for ab in AB:
        if (K - ab) in CD:
            ok = True

    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
