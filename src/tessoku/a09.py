import itertools


class CumulativeSum2D:
    def __init__(self, h: int, w: int) -> None:
        self.h = h
        self.w = w
        self.body = [[0 for i in range(w + 1)] for i in range(h + 1)]

    def add(self, r: int, c: int, v: int) -> None:
        self.body[r][c] += v

    def build(self) -> None:
        for i, j in itertools.product(range(self.h + 1), range(1, self.w + 1)):
            self.body[i][j] += self.body[i][j - 1]
        for j, i in itertools.product(range(self.w + 1), range(1, self.h + 1)):
            self.body[i][j] += self.body[i - 1][j]


def main() -> None:
    H, W, N = map(int, input().split())
    A, B, C, D = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    c2d = CumulativeSum2D(H + 1, W + 1)
    for a, b, c, d in zip(A, B, C, D):
        c2d.add(a, b, 1)
        c2d.add(a, d + 1, -1)
        c2d.add(c + 1, b, -1)
        c2d.add(c + 1, d + 1, 1)

    c2d.build()

    for row in c2d.body[1:-1]:
        print(*row[1:-1])


if __name__ == "__main__":
    main()
