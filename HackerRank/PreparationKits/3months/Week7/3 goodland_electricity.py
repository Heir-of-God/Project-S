import os


def pylons(k: int, arr: list[int]) -> int:
    last_unpowered_ind = 0
    last_can_build_station = -1
    k -= 1
    res = 0

    for ind, city in enumerate(arr):
        last_can_build_station = ind if city == 1 else last_can_build_station
        if last_unpowered_ind + k == ind or (ind == len(arr) - 1):
            if last_can_build_station == -1:
                return -1
            res += 1
            last_unpowered_ind = last_can_build_station + k + 1
            if last_unpowered_ind > len(arr) - 1:
                break
            last_can_build_station = -1

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pylons(k, arr)
    fptr.write(str(result) + "\n")
    fptr.close()
