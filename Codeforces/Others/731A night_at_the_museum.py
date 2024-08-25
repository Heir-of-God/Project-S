s = input()
res = 0
cur = ord("a")

for char in s:
    char_val = ord(char)
    rotates_to_char = min(abs(char_val - cur), abs(26 - (abs(char_val - cur))))
    res += rotates_to_char
    cur = char_val

print(res)
