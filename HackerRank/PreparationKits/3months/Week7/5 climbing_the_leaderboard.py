import os


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    result: list[int] = []
    cur_ind: int = 0
    current_place: int = 1
    player_ind: int = len(player) - 1
    ranked.append(0)

    while cur_ind < len(ranked):
        if player_ind < 0:
            return result

        last_score = ranked[cur_ind]
        if player[player_ind] >= last_score:
            result = [current_place] + result
            player_ind -= 1
        else:
            cur_ind += 1
            if ranked[cur_ind] != last_score:
                current_place += 1

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
