s1 = input().lower()
s2 = input().lower()
n = len(s1)

for char_ind in range(n):
    ch1 = ord(s1[char_ind])
    ch2 = ord(s2[char_ind])

    if ch1 > ch2:
        print(1)
        exit()
    elif ch2 > ch1:
        print(-1)
        exit()

print(0)
