t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]

    for ind in range(1, n, 1):
        if arr[ind - 1] != arr[ind]:
            break

    if ind != 1 or arr[0] == arr[-1]:
        print(ind + 1)
    else:
        print(1)
