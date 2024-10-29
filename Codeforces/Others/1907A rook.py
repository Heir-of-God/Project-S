t = int(input())

for _ in range(t):
    pos = input()

    for letter in "abcdefgh":
        if letter != pos[0]:
            print(letter + pos[1])

    for num in range(1, 9, 1):
        num = str(num)
        if num != pos[1]:
            print(pos[0] + num)
