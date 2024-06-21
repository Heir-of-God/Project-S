def strings_xor(s: str, t: str) -> str:
    res: str = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += "0"
        else:
            res += "1"

    return res


s: str = input()
t: str = input()
print(strings_xor(s, t))
