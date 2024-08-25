import os
from collections import deque


def solve(arr: list[int], queries: list[int]) -> list[int]:
    res: list[int] = []

    for num in queries:
        cur_mn_max: int = float("inf")
        stack: list[tuple[int, int]] = deque([])

        for ind, el in enumerate(arr):
            while stack and stack[-1][1] <= el:
                stack.pop()
            stack.append((ind, el))

            while stack and stack[0][0] < ind - num + 1:
                stack.popleft()

            if ind >= num - 1:
                cur_mn_max = min(cur_mn_max, stack[0][1])

        res.append(cur_mn_max)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = solve(arr, queries)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
