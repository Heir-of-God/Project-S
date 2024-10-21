t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    cur_sum = sum(arr)

    if cur_sum >= n:
        print(cur_sum - n)
    else:
        print(1)
