t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    seen = set([arr[0]])
    res = "YES"

    for n in arr[1:]:
        seen.add(n)
        if not (n - 1 in seen or n + 1 in seen):
            res = "NO"
            break

    print(res)
