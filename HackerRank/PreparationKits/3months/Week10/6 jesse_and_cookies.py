import os
import heapq


def cookies(need: int, cookies: list[int]) -> int:
    heapq.heapify(cookies)

    res = 0
    while len(cookies) >= 2 and cookies[0] < need:
        first_min = heapq.heappop(cookies)
        second_min = heapq.heappop(cookies)
        new = first_min + 2 * second_min
        heapq.heappush(cookies, new)
        res += 1

    return res if cookies[0] >= need else -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    A = list(map(int, input().rstrip().split()))
    result = cookies(k, A)
    fptr.write(str(result) + "\n")
    fptr.close()
