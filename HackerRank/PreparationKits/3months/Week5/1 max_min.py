import os


def maxMin(k: int, arr: list[int]) -> int:
    arr.sort()
    res = float("inf")

    for end_ind in range(k - 1, len(arr), 1):
        res = min(res, arr[end_ind] - arr[end_ind - k + 1])

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + "\n")
    fptr.close()
