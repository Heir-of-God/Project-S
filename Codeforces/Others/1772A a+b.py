t = int(input())

for _ in range(t):
    s = input()
    nums = [int(i) for i in s.split("+")]
    print(sum(nums))
