s1 = input()
s2 = input()
s = input()
matching = {s1[i]: s2[i] for i in range(26)}
res = ""

for char in s:
    if char.lower() in matching:
        add = matching[char.lower()]
        if char.isupper():
            add = add.upper()
        res += add
    else:
        res += char

print(res)
