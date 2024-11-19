t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = ""

    prev = ""
    for char in s:
        if prev == "":
            res += char
            prev = char
        elif prev == char:
            prev = ""

    print(res)
