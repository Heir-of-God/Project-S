n, power = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
arr.sort()
right = n - 1
left = 0
res = 0

while left <= right:
    cur_strongest = arr[right]
    other_players = right - left
    need_players = power // cur_strongest
    if need_players > other_players:
        break
    res += 1
    left += need_players
    right -= 1

print(res)
