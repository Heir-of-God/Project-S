import os


def hackerlandRadioTransmitters(coordinates: list[int], distance_range: int) -> int:
    coordinates.sort()
    n: int = len(coordinates)
    res: int = 0
    cur_ind: int = 0

    while cur_ind != n:
        res += 1
        start: int = coordinates[cur_ind]
        while cur_ind != n - 1 and coordinates[cur_ind + 1] - start <= distance_range:
            cur_ind += 1
        start = coordinates[cur_ind]
        while cur_ind != n - 1 and coordinates[cur_ind + 1] - start <= distance_range:
            cur_ind += 1

        cur_ind += 1

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    x = list(map(int, input().rstrip().split()))
    result = hackerlandRadioTransmitters(x, k)
    fptr.write(str(result) + "\n")
    fptr.close()
