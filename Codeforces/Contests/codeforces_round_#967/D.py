from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    inp = [int(ind) for ind in input().split()]

    last_position = [-1 for _ in range(n + 1)]
    value_indices = defaultdict(list)

    for ind in range(n):
        last_position[inp[ind]] = ind + 1
        value_indices[inp[ind]].append(ind + 1)

    counter = [0 for _ in range(n + 1)]
    nxt_ind_to_check = float("inf")

    for ind in range(1, n + 1):
        if last_position[ind] != -1:
            counter[last_position[ind]] += 1
            nxt_ind_to_check = min(nxt_ind_to_check, last_position[ind])

    visited = [False for _ in range(n + 1)]
    res = []
    ind = 1

    while ind <= n:
        if ind == nxt_ind_to_check:
            res.append(inp[ind - 1])
            counter[last_position[inp[ind - 1]]] -= 1
            while nxt_ind_to_check <= n and counter[nxt_ind_to_check] == 0:
                nxt_ind_to_check += 1
            ind += 1
        else:
            end = min(nxt_ind_to_check, n) + 1
            valid_vals = [inp[j - 1] for j in range(ind, end) if not visited[j]]
            if not valid_vals:
                break
            target_val = max(valid_vals) if len(res) % 2 == 0 else min(valid_vals)
            ind = next(j + 1 for j in range(ind, end) if inp[j - 1] == target_val)
            res.append(target_val)
            counter[last_position[target_val]] -= 1
            while nxt_ind_to_check <= n and counter[nxt_ind_to_check] == 0:
                nxt_ind_to_check += 1

        for index in value_indices[res[-1]]:
            visited[index] = True

    print(len(res))
    print(" ".join(map(str, res)))
