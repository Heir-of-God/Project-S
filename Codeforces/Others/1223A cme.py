q = int(input())

for _ in range(q):
    n = int(input())
    if n < 4:
        print(4 - n)
    elif n & 1 == 0:
        print(0)
    else:
        print(1)
