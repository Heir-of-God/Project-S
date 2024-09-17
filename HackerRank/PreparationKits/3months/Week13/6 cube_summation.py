import os


def cubeSum(n: int, operations: list[str]) -> list[int]:
    res: list[int] = []
    positions: dict[tuple[int, int, int], int] = {}
    for op in operations:
        inp = op.split(" ")
        if inp[0] == "UPDATE":
            x, y, z, w = [int(i) for i in inp[1:]]
            positions[(x, y, z)] = w

        elif inp[0] == "QUERY":
            x1, y1, z1, x2, y2, z2 = [int(i) for i in inp[1:]]
            sm = 0
            for x, y, z in positions:
                if x2 >= x >= x1 and y2 >= y >= y1 and z2 >= z >= z1:
                    sm += positions[(x, y, z)]
            res.append(sm)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    T = int(input().strip())
    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()
        matSize = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        ops = []
        for _ in range(m):
            ops_item = input()
            ops.append(ops_item)
        res = cubeSum(matSize, ops)
        fptr.write("\n".join(map(str, res)))
        fptr.write("\n")
    fptr.close()
