t = int(input())


for _ in range(t):
    n = int(input())
    beautiful_array = list(range(1, n + 1))
    print(" ".join(map(str, beautiful_array)))
