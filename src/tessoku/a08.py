import itertools


class CumulativeSum2D:
    def __init__(self, h: int, w: int) -> None:
        """
        Args:
        - h (int): Height of the matrix.
        - w (int): Width of the matrix.
        """
        self.h = h
        self.w = w
        self.body = [[0 for i in range(w + 1)] for i in range(h + 1)]

    def set(self, r: int, c: int, v: int) -> None:
        """
        Set the value for the specified cell.

        Args:
        - r (int): The index of the row for which the value will be set (1-indexed).
        - c (int): The index of the column for which the value will be set (1-indexed).
        - v (int): The value which will be set for the cell.
        """
        self.body[r][c] = v

    def build(self) -> None:
        """
        Build cumulative sum.
        """
        for i, j in itertools.product(range(0, self.h + 1), range(0, self.w + 1)):
            s = 0
            if i > 0:
                s += self.body[i - 1][j]
            if j > 0:
                s += self.body[i][j - 1]
            if i > 0 and j > 0:
                s -= self.body[i - 1][j - 1]
            self.body[i][j] += s

    def get(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        right_open=False,
    ) -> int:
        """
        Get cumulative sum of the area represented by the start and end cell.

        Args:
        - start (tuple[int, int]): The index of the start cell (1-indexed).
        - end (tuple[int, int]): The index of the end cell (1-indexed).
        - right_open (bool): If true, get right-opened cumulative sum.
        """
        sr, sc = start
        er, ec = end

        if right_open:
            result = self.body[er - 1][ec - 1]
            if sr > 0:
                result -= self.body[sr - 1][ec - 1]
            if sc > 0:
                result -= self.body[er - 1][sc - 1]
            if sr > 0 and sc > 0:
                result += self.body[sr - 1][sc - 1]
            return result
        else:
            result = (
                self.body[er][ec]
                - self.body[sr][ec]
                - self.body[er][sc]
                + self.body[sr][sc]
            )
            return result


def main() -> None:
    H, W = map(int, input().split())
    X: list[list[int]] = [[int(v.strip()) for v in input().split()] for i in range(H)]
    Q: int = int(input())
    A, B, C, D = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    c2d = CumulativeSum2D(H, W)

    for i, row in enumerate(X, 1):
        for j, x in enumerate(row, 1):
            c2d.set(i, j, x)
    c2d.build()

    for a, b, c, d in zip(A, B, C, D):
        print(c2d.get((a - 1, b - 1), (c, d)))


if __name__ == "__main__":
    main()
