price, k = [int(i) for i in input().split()]
res = 1

while (price * res) % 10 not in [0, k]:
    res += 1

print(res)
