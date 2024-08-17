n = int(input())

res = n // 2

if n & 1 == 1:
    res -= 1

print(res if n & 1 == 0 else res + 1)
print(" ".join(["2" for _ in range(res)]) + ("" if n & 1 == 0 else " 3"))
