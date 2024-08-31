n, t = [int(i) for i in input().split()]

num = 10 ** (n - 1)
if num == 1 and t == 10:
    print(-1)
    exit()

if t == 10:
    print(num)
else:
    print(num * t)
