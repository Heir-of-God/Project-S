import os


def min_operations(n: int, boxes: list[list[int]]) -> int:
    if n <= 2:
        return -1
    colors_sums: list[int] = [0, 0, 0]
    color_maxs: list[int] = [0, 0, 0]

    for box in boxes:
        for ind, num in enumerate(box):
            colors_sums[ind] += num
            color_maxs[ind] = max(color_maxs[ind], num)

    return sum([colors_sums[i] - color_maxs[i] for i in range(3)])


fptr = open(os.environ["OUTPUT_PATH"], "w")
n = int(input().strip())
boxes = []
for _ in range(n):
    boxes.append(list(map(int, input().rstrip().split())))
result = min_operations(n, boxes)
fptr.write(str(result) + "\n")
fptr.close()
