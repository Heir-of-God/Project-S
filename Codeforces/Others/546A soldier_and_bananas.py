k, n, w = input().split()
w = int(w)
k = int(k)
n = int(n)
res = k * (w * (w + 1) // 2)

print(res - n if res >= n else 0)
