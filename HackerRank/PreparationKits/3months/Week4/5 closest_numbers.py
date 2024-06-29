import os


def closestNumbers(arr: list[int]) -> list[int]:
    n: int = len(arr)
    arr.sort()
    res: list[int] = []
    mn_abs: int = float("inf")
    for ind in range(n - 1):
        if arr[ind + 1] - arr[ind] < mn_abs:
            mn_abs = arr[ind + 1] - arr[ind]
    for ind in range(n - 1):
        if arr[ind + 1] - arr[ind] == mn_abs:
            res.append(arr[ind])
            res.append(arr[ind + 1])

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
