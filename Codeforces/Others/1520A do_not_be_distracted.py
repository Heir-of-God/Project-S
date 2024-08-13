t = int(input())

for _ in range(t):
    n = int(input())
    tasks = input()
    seen = set()
    tasks = "." + tasks

    res = False
    for ind in range(1, n + 1):
        cur = tasks[ind]
        prev = tasks[ind - 1]

        if cur in seen:
            res = True
            break
        elif cur != prev:
            seen.add(prev)

    print("NO" if res else "YES")
