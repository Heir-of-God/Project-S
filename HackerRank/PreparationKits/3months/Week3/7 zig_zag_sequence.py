def findZigZagSequence(a, n) -> None:
    a.sort()
    mid: int = n // 2
    a[mid], a[n - 1] = a[n - 1], a[mid]

    to_change: int = mid + 1
    from_change: int = n - 2
    while to_change < from_change:
        a[to_change], a[from_change] = a[from_change], a[to_change]
        to_change += 1
        from_change -= 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
