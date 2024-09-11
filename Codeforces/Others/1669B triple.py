t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    count = [0 for _ in range(n + 1)]

    flag = True
    for el in arr:
        count[el] += 1
        if count[el] == 3:
            print(el)
            flag = False
            break

    if flag:
        print(-1)
