t = int(input())

for _ in range(t):
    time = [int(i) for i in input().split(":")]
    time = time[0] * 60 + time[1]

    if time == 60 * 12:
        print("12:00 PM")
        continue
    elif time == 0:
        print("12:00 AM")
        continue

    after = time > 60 * 12
    time_left = time % (60 * 12) if not (60 * 12 < time < 60 * 13) else time

    if 0 < time < 60:
        time_left += 60 * 12

    print(f"{time_left // 60:02d}:{time_left % 60:02d} {'AM' if not after else 'PM'}")
