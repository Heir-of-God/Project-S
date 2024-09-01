n = int(input())
arr = [int(i) for i in input().split()]

count = {1: 0, 2: 0, 3: 0, 4: 0}
for num in arr:
    count[num] += 1

res = count[4]
groups31 = min(count[3], count[1])
res += groups31
count[3] -= groups31
count[1] -= groups31
res += count[3]
res += count[2] // 2
count[2] %= 2
if count[2]:
    res += 1
    count[2] -= 1
    if count[1]:
        count[1] -= 2
count[1] = max(count[1], 0)
if count[1]:
    res += (count[1] + 3) // 4

print(res)
