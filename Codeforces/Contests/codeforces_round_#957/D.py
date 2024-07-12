t = int(input())

for _ in range(t):
    river_length, max_jump, freeze_time = [int(i) for i in input().split()]
    river = ["L"] + list(input())

    cur_ind = 0
    possible = True
    while possible and cur_ind != river_length + 1:
        if river[cur_ind] == "W":
            freeze_time -= 1
            if freeze_time < 0:
                possible = False
            cur_ind += 1
        elif river[cur_ind] == "C":
            possible = False
        elif river[cur_ind] == "L":
            if cur_ind + max_jump >= river_length + 1:
                break
            most_optimal_position = None
            seen_crocodile = False
            for possible_ind in range(cur_ind + max_jump, cur_ind, -1):
                if river[possible_ind] == "L":
                    most_optimal_position = possible_ind
                    break
                elif river[possible_ind] == "C":
                    seen_crocodile = True
                elif not seen_crocodile and river[possible_ind] == "W" and most_optimal_position is None:
                    most_optimal_position = possible_ind
            if most_optimal_position is None:
                possible = False
            cur_ind = most_optimal_position

    print("YES" if possible else "NO")
