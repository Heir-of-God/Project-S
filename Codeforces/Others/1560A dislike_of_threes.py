t = int(input())
nums = [i for i in range(1, 1667, 1) if i % 10 != 3 and i % 3 != 0]

for _ in range(t):
    print(nums[int(input()) - 1])
