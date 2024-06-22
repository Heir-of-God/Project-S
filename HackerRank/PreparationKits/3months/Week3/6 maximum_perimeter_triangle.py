import os


def maximumPerimeterTriangle(sticks: list[int]) -> list[int]:
    sticks.sort()
    n: int = len(sticks)
    for biggest_side_ind in range(n - 1, 1, -1):
        if sticks[biggest_side_ind] < sticks[biggest_side_ind - 1] + sticks[biggest_side_ind - 2]:
            return [sticks[biggest_side_ind - 2], sticks[biggest_side_ind - 1], sticks[biggest_side_ind]]
    return [-1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
