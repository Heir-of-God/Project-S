t = int(input())

for _ in range(t):
    keys = input()
    s = input()
    inds = {}

    for ind, char in enumerate(keys):
        inds[char] = ind

    res = 0
    for ind in range(1, len(s)):
        res += abs(inds[s[ind]] - inds[s[ind - 1]])

    print(res)
