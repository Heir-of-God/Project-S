t = int(input())

for _ in range(t):
    c = int(input())
    arr = [int(i) for i in input().split()]
    one = 0
    two = 0

    for el in arr:
        if el == 1:
            one += 1
        else:
            two += 1

    print("NO" if one & 1 == 1 or two & 1 == 1 and one == 0 else "YES")
