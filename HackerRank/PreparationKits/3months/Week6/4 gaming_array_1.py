import os


def gamingArray(arr: list[int]) -> str:
    count_max: int = 0
    last_max: int = 0
    for a in arr:
        if a > last_max:
            last_max = a
            count_max += 1
    return "ANDY" if count_max % 2 == 0 else "BOB"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    g = int(input().strip())
    for g_itr in range(g):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = gamingArray(arr)
        fptr.write(result + "\n")
    fptr.close()
