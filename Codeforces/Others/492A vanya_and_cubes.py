n = int(input())
nxt_level = 1
res = 0

while n >= nxt_level:
    res += 1
    n -= nxt_level
    nxt_level += res + 1


print(res)
