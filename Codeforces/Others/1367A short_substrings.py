t = int(input())


for _ in range(t):
    b = input()
    res = [b[0]]

    for ind in range(1, len(b) - 2 + 1, 2):
        res.append(b[ind])

    res.append(b[-1])

    print("".join(res))
