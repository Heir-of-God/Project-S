t = int(input())

for _ in range(t):
    _, rounds = [int(i) for i in input().split()]
    problems = input()
    count = {char: 0 for char in "ABCDEFG"}

    for problem in problems:
        count[problem] += 1

    res = 0
    for k in count.values():
        res += max(rounds - k, 0)

    print(res)
