t = int(input())

for _ in range(t):
    n, f, k = [int(i) for i in input().split()]
    vals = [int(i) for i in input().split()]
    fav_val = vals[f - 1]
    vals.sort(reverse=True)

    count = vals.count(fav_val)
    first = vals.index(fav_val)

    if k <= first:
        print("NO")
    elif k >= first + count:
        print("YES")
    else:
        print("MAYBE")
