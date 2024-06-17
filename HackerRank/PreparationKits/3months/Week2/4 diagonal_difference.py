import os


def diagonalDifference(arr: list[list[int]]) -> int:
    res: int = 0
    n: int = len(arr)
    left: int = 0
    right: int = n - 1

    for row in arr:
        res += row[left]
        res -= row[right]
        left += 1
        right -= 1

    return abs(res)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + "\n")
    fptr.close()
