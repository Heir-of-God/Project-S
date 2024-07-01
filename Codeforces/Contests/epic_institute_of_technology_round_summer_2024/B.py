t = int(input())


def min_coins_to_sort(arr):
    res = 0
    cur_max = 0
    add = 0

    for el in arr:
        res += max(0, cur_max - el)
        add = max(add, cur_max - el)
        cur_max = max(cur_max, el)

    return res + add


for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(min_coins_to_sort(a))
