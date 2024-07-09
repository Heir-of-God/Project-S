friends_num, height = map(int, input().split())
friends = [int(i) for i in input().split()]
res = friends_num

for friend in friends:
    if friend > height:
        res += 1

print(res)
