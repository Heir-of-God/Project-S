n = int(input())
grades = [int(i) for i in input().split()]

cur_sum = sum(grades)
need_sum = n * 4.5

grades_count = [0, 0, 0, 0]
for grade in grades:
    grades_count[grade - 2] += 1

res = 0
if cur_sum < need_sum:
    for num, val in zip(grades_count[:-1], [3, 2, 1]):
        can_get = num * val
        if can_get + cur_sum < need_sum:
            cur_sum += can_get
            res += num
        else:
            times = int(need_sum - cur_sum) // val
            cur_sum += times * val
            res += times + (cur_sum < need_sum)
            break

print(res)
