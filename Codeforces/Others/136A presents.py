n = int(input())
friends = [int(i) for i in input().split()]
res = [0 for _ in range(n)]

for cur_num in range(1, n + 1, 1):
    ind = cur_num - 1
    res[friends[ind] - 1] = cur_num

print(" ".join([str(i) for i in res]))
