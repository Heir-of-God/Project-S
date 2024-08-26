t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    deleted = 0

    for ind in range(n // 2):
        reversed_ind = n - ind - 1
        if s[ind] != s[reversed_ind]:
            deleted += 2
        else:
            break

    print(n - deleted)
