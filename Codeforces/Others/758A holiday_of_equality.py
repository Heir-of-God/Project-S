n = int(input())
money = [int(i) for i in input().split()]
res = 0
mx = max(money)

for m in money:
    res += mx - m

print(res)
