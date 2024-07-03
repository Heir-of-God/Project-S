w1, w2 = input().split()
w1 = int(w1)
w2 = int(w2)
res = 0

while w1 <= w2:
    w1 *= 3
    w2 *= 2
    res += 1

print(res)
