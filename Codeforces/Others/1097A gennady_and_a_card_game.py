on_table = input()
hand = input().split()

res = "NO"
for card in hand:
    if card[0] == on_table[0] or card[1] == on_table[1]:
        res = "YES"
        break

print(res)
