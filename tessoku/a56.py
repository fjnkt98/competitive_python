import sys

input = sys.stdin.readline


class HashedString:
    def __init__(self, s: str, p: int) -> None:
        s = [ord(c) - ord("a") for c in s]
        n = len(s)

        x = [1] * (n + 1)
        h = [0] * (n + 1)
        for i in range(1, n + 1):
            x[i] = (100 * x[i - 1]) % p
            h[i] = (h[i - 1] * 100 + s[i - 1]) % p

        self.s = s
        self.p = p
        self.x = x
        self.h = h

    def hash(self, l: int, r: int) -> int:
        h = self.h[r] - self.x[r - l + 1] * self.h[l - 1]
        while h < 0:
            h += self.p
        h %= self.p
        return h


def main() -> None:
    N, Q = map(int, input().split())
    S: str = input().rstrip()
    p = 2147483647
    hs = HashedString(S, p)

    for _ in range(Q):
        a, b, c, d = map(int, input().split())

        h1 = hs.hash(a, b)
        h2 = hs.hash(c, d)

        if h1 == h2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
