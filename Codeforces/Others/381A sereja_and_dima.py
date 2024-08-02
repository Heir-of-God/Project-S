n = int(input())
cards = [int(i) for i in input().split()]
left = 0
right = n - 1
sereja_moves = True
sereja = 0
dima = 0

while left <= right:
    if cards[left] < cards[right]:
        sereja += sereja_moves * cards[right]
        dima += (not sereja_moves) * cards[right]
        right -= 1
    else:
        sereja += sereja_moves * cards[left]
        dima += (not sereja_moves) * cards[left]
        left += 1
    sereja_moves = not sereja_moves

print(sereja, dima)
