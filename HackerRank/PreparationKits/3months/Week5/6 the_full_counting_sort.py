def countSort(arr):
    arr_sort: list[list[str]] = [[] for _ in range(100)]
    arr_len: int = len(arr)
    for ind in range(arr_len):
        pos = int(arr[ind][0])
        string = arr[ind][1]
        if ind < arr_len // 2:
            arr_sort[pos].append("-")
        else:
            arr_sort[pos].append(string)

    res: list[str] = [el for pos_list in arr_sort for el in pos_list]
    print(" ".join(res))


if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
