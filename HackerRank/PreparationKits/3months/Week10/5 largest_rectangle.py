import os


def largestRectangle(heights: list[int]) -> int:
    res = 0
    stack = []  # (start_range_ind, height)
    heights.append(0)

    for ind, height in enumerate(heights):
        range_start = ind

        while stack and stack[-1][1] >= height:
            start_ind, prev_height = stack.pop()
            res = max(res, prev_height * (ind - start_ind))
            range_start = start_ind

        stack.append((range_start, height))

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    fptr.write(str(result) + "\n")
    fptr.close()
