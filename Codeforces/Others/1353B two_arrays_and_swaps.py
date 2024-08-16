t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]

    arr1.sort()
    arr2.sort()

    s = sum(arr1)
    kbiggest2 = arr2[n - k :]

    for ind in range(k):
        if arr1[ind] < kbiggest2[-ind - 1]:
            s -= arr1[ind]
            s += kbiggest2[-ind - 1]

    print(s)
