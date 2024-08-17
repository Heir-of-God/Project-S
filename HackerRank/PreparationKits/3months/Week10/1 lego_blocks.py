import os


def legoBlocks(rows: int, cols: int) -> int:
    MOD = 10**9 + 7
    buld_one_row: list[int] = [1, 1, 2, 4]

    for width in range(4, cols + 1, 1):
        buld_one_row.append(sum(buld_one_row[-4:]) % MOD)
    build_a_wall: list[int] = [(ways**rows) % MOD for ways in buld_one_row]

    valid: list[int] = build_a_wall[:]
    for width in range(cols + 1):
        for first_half in range(1, width):
            valid[width] -= valid[first_half] * build_a_wall[width - first_half]
        valid[width] %= MOD

    return valid[cols]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        rows = int(first_multiple_input[0])
        cols = int(first_multiple_input[1])
        result = legoBlocks(rows, cols)
        fptr.write(str(result) + "\n")
    fptr.close()
