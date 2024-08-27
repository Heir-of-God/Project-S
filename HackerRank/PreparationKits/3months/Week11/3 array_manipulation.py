import os


def arrayManipulation(n: int, queries: list[list[int]]) -> int:
    arr: list[int] = [0 for _ in range(n + 1)]
    for start, end, num in queries:
        arr[start - 1] += num
        arr[end] -= num

    res: int = 0
    cur_sum: int = 0
    for num in arr:
        cur_sum += num
        if cur_sum > res:
            res = cur_sum

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + "\n")
    fptr.close()
