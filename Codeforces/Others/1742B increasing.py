t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    seen = set()
    flag = True

    for el in arr:
        if el not in seen:
            seen.add(el)
        else:
            flag = False
            break

    print("YES" if flag else "NO")
