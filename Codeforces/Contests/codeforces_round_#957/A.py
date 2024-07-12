t = int(input())

for _ in range(t):
    nums = [int(i) for i in input().split()]
    for _ in range(5):
        mn = min(nums)
        ind = nums.index(mn)
        nums[ind] += 1
    print(nums[0] * nums[1] * nums[2])
