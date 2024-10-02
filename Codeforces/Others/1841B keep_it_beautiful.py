t = int(input())

for _ in range(t):
    q = int(input())
    nums = [int(i) for i in input().split()]
    cur = []
    cnt = 0
    res = ""

    for num in nums:
        nw_cnt = cnt + (len(cur) > 0 and cur[-1] > num)
        if nw_cnt == 0 or (nw_cnt == 1 and num <= cur[0]):
            cur.append(num)
            cnt = nw_cnt
            res += "1"
        else:
            res += "0"

    print(res)
