import os


def get_index(num, nums):
    left = 0
    right = len(nums) - 1
    res = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == num:
            return mid

        elif nums[mid] > num:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res


def runningMedian(a: list[int]) -> int:
    nums = []
    odd = True
    res = []
    for el in a:
        nums.insert(get_index(el, nums), el)
        res.append(f"{(nums[len(nums) // 2] if odd else (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2):.1f}")
        odd = not odd
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    a_count = int(input().strip())
    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)
    result = runningMedian(a)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
