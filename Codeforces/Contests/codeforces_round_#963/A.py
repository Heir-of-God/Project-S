t = int(input())

for _ in range(t):
    count = {}
    n = int(input())
    s = input()
    for char in s:
        if char != "?":
            if char not in count:
                count[char] = 0
            count[char] += 1

    res = 0
    for c in count.values():
        res += min(c, n)

    print(res)
