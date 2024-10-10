t = int(input())

for _ in range(t):
    nums = [int(i) for i in input().split()]
    nums.sort()
    if nums[1] != nums[2]:
        print("NO")
    else:
        print("YES")
        print(nums[0], nums[0], nums[2])
