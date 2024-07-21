import os


def bomberMan(n: int, grid: list[str]) -> list[str]:
    rows: int = len(grid)
    cols: int = len(grid[0])

    bombs = set((r_ind, c_ind) for r_ind in range(rows) for c_ind in range(cols) if grid[r_ind][c_ind] == "O")
    bombs_everywhere = set((r_ind, c_ind) for r_ind in range(rows) for c_ind in range(cols))

    def get_next_state(bomb_locations) -> set[tuple[int, int]]:
        next_state: set[tuple[int, int]] = bombs_everywhere.copy()
        for r_ind, c_ind in bomb_locations:
            next_state.discard((r_ind, c_ind))
            next_state.discard((r_ind - 1, c_ind))
            next_state.discard((r_ind + 1, c_ind))
            next_state.discard((r_ind, c_ind + 1))
            next_state.discard((r_ind, c_ind - 1))
        return next_state

    def convert_to_grid(set_representation) -> list[str]:
        return ["".join(["O" if (r, c) in set_representation else "." for c in range(cols)]) for r in range(rows)]

    if n == 1:
        return grid
    if n % 2 == 0:
        return convert_to_grid(bombs_everywhere)
    if n % 4 == 3:
        return convert_to_grid(get_next_state(bombs))
    else:
        return convert_to_grid(get_next_state(get_next_state(bombs)))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    result = bomberMan(n, grid)
    fptr.write("\n".join(result))
    fptr.write("\n")
    fptr.close()
