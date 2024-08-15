import os
from math import ceil


def chiefHopper(arr: list[int]) -> int:
    cur_energy = 0

    for el in arr[::-1]:
        cur_energy = ceil((el + cur_energy) / 2)

    return cur_energy


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = chiefHopper(arr)
    fptr.write(str(result) + "\n")
    fptr.close()
