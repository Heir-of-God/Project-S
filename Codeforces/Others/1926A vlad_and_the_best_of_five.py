t = int(input())

for _ in range(t):
    s = input()
    count = [0, 0]
    for char in s:
        count[ord(char) - ord("A")] += 1

    print("A" if count[0] > count[1] else "B")
