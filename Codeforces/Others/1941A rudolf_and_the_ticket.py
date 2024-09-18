t = int(input())


def binary_search(lst, value_insert):
    left = 0
    right = len(lst) - 1
    res = 0

    while left <= right:
        mid = (left + right) // 2
        val = lst[mid]

        if val <= value_insert:
            res = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    return res


for _ in range(t):
    a, b, need = [int(i) for i in input().split()]
    left = [int(i) for i in input().split()]
    right = [int(i) for i in input().split()]
    left.sort()
    right.sort()
    res = 0

    for val in left:
        to_add_max = need - val
        if to_add_max <= 0:
            break
        good_elems = binary_search(right, to_add_max)
        res += good_elems

    print(res)
