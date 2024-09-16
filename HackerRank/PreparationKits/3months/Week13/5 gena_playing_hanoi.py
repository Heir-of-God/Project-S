import os
import math


def hanoi(posts):
    n = len(posts)
    rods = [0, 0, 0, 0]
    for i in range(n):
        rods[posts[i] - 1] += 2**i
    base = 2**n
    win_state = (base - 1) * (base**3)
    start_state = rods[0] * (base**3) + rods[1] * (base**2) + rods[2] * base + rods[3]
    visited = set()
    current = [start_state]
    moves = 0
    while len(current) > 0:
        next = []
        for state in current:
            if state == win_state:
                return moves
            if state in visited:
                continue
            visited.add(state)
            rods = [(state // base**3) % base, (state // base**2) % base, (state // base) % base, state % base]
            top_discs = [math.inf if n == 0 else n ^ (n & (n - 1)) for n in rods]
            for i in range(4):
                for j in range(i + 1, 4):
                    if top_discs[i] == math.inf and top_discs[j] == math.inf:
                        continue
                    if top_discs[i] < top_discs[j]:
                        new_state = state - top_discs[i] * (base ** (3 - i)) + top_discs[i] * (base ** (3 - j))
                    else:
                        new_state = state + top_discs[j] * (base ** (3 - i)) - top_discs[j] * (base ** (3 - j))
                    if new_state not in visited:
                        next.append(new_state)
        moves += 1
        current = next


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    loc = list(map(int, input().rstrip().split()))
    res = hanoi(loc)
    fptr.write(str(res) + "\n")
    fptr.close()
