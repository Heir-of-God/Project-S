res = 0
letters = set()
s = input()

for char in s:
    if char in ", {}":
        continue
    if char not in letters:
        letters.add(char)
        res += 1

print(res)
