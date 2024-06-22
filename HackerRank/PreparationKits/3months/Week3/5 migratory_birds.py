import os


def migratoryBirds(arr: list[int]) -> int:
    count: list[int] = [0 for _ in range(5)]  # There are only 5 types of birds
    for n in arr:
        count[n - 1] += 1
    mx: int = 0
    res: int = 1
    for type_id, n in enumerate(count, 1):
        if n > mx:
            mx = n
            res = type_id

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + "\n")
    fptr.close()
