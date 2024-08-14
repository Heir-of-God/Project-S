t = int(input())

for _ in range(t):
    rows, cols, kside = [int(i) for i in input().split()]
    n = int(input())
    heights = [int(i) for i in input().split()]

    temp = []

    for i in range(rows):
        for j in range(cols):
            value = (kside - max(kside - i - 1, 0)) - max(kside - (rows - i), 0)
            value *= (kside - max(kside - j - 1, 0)) - max(kside - (cols - j), 0)
            temp.append(value)

    temp.sort(reverse=True)
    heights.sort(reverse=True)

    res = 0
    for i in range(n):
        res += temp[i] * heights[i]

    print(res)
