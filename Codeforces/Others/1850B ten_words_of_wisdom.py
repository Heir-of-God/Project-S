t = int(input())

for _ in range(t):
    n = int(input())
    words = []
    quality = []
    for _ in range(n):
        a, b = input().split()
        words.append(int(a))
        quality.append(int(b))

    res = -1
    mx = 0
    for i, (num_of_words, q) in enumerate(zip(words, quality)):
        if num_of_words <= 10 and q > mx:
            res = i + 1
            mx = q

    print(res)
