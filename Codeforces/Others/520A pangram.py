_ = input()
s = set(list(input()))

for char_add in range(0, 26, 1):
    if not chr(ord("a") + char_add) in s and not chr(ord("A") + char_add) in s:
        print("NO")
        exit()

print("YES")
