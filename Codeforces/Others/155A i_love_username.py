_ = input()
points = [int(i) for i in input().split()]

minimum = points[0]
maximum = points[0]
res = 0

for ind in range(1, len(points)):
    p = points[ind]
    if p > maximum:
        maximum = p
        res += 1
    elif p < minimum:
        minimum = p
        res += 1

print(res)
