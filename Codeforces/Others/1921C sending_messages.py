t = int(input())

for _ in range(t):
    n, charge_left, time_fee, turn_fee = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    res = 0
    last_time = 0
    for time in arr:
        dont_turn_off = (time - last_time) * time_fee
        res += min(dont_turn_off, turn_fee)
        last_time = time

    print("YES" if res < charge_left else "NO")
