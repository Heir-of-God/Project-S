overall_time = 60 * 4
n, k = [int(i) for i in input().split()]
overall_time -= k
res = 0

while res != n and overall_time - (res + 1) * 5 >= 0:
    overall_time -= (res + 1) * 5
    res += 1

print(res)
