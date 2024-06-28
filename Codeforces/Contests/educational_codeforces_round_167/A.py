coins = int(input())


def can_collect_coin(x, y):
    return "YES" if y - x >= -x - 1 else "NO"


res = []
for _ in range(coins):
    x, y = input().split()
    x = int(x)
    y = int(y)
    res.append(can_collect_coin(x, y))

for i in res:
    print(i)
