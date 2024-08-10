r = int(input())
res1 = 0
res2 = 0

for _ in range(r):
    m, c = [int(i) for i in input().split()]
    if m > c:
        res1 += 1
    elif c > m:
        res2 += 1

print("Mishka" if res1 > res2 else "Chris" if res2 > res1 else "Friendship is magic!^^")
