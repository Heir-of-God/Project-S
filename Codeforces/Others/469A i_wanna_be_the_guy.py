levels = int(input())
player1 = set([int(i) for i in input().split()[1:]])
player2 = set([int(i) for i in input().split()[1:]])

for level in range(1, levels + 1, 1):
    if not level in player1 and not level in player2:
        print("Oh, my keyboard!")
        exit()

print("I become the guy.")
