t = int(input())

for _ in range(t):
    tasks_n, for_shower, m = [int(i) for i in input().split()]
    tasks = []
    for _ in range(tasks_n):
        tasks.append([int(i) for i in input().split()])
    tasks.sort()
    last_task_ended = 0

    res = False
    for start, end in tasks:
        if start - last_task_ended >= for_shower:
            res = True
            break
        last_task_ended = end

    if not res:
        res = m - last_task_ended >= for_shower

    print("YES" if res else "NO")
