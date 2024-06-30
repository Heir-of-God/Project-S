import os


def minimumAbsoluteDifference(arr: list[int]) -> int:
    arr.sort()
    n: int = len(arr)
    res: int = float("inf")

    for ind in range(1, n, 1):
        dif = arr[ind] - arr[ind - 1]
        if dif < res:
            res = dif

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + "\n")
    fptr.close()
