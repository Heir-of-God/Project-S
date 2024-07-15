import os


def formingMagicSquare(s: list[list[int]]) -> int:
    all_magic_squares: list[list[list[int]]] = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    results: list[int] = []
    for magic_square in all_magic_squares:
        res = 0
        for row_ind in range(3):
            for col_ind in range(3):
                res += abs(s[row_ind][col_ind] - magic_square[row_ind][col_ind])
        results.append(res)

    return min(results)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    fptr.write(str(result) + "\n")
    fptr.close()
