n = int(input())
res = 0

for bill in [100, 20, 10, 5, 1]:
    if n == 0:
        break
    res += n // bill
    n -= (n // bill) * bill

print(res)
