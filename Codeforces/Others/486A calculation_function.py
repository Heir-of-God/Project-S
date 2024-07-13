inp = int(input())
n = inp // 2
res = 0 if inp & 1 == 0 else -inp
res += 1 * n

print(res)
