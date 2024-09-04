class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacles = set([tuple(i) for i in obstacles])
        dirs: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        coords: list[int] = [0, 0]
        res: int = 0
        moved = False

        for step in commands:
            if step > 0:
                while step > 0 and (tuple(coords) not in obstacles or not moved):
                    coords[0] += dirs[cur_dir][0]
                    coords[1] += dirs[cur_dir][1]
                    step -= 1
                    moved = True
                if tuple(coords) in obstacles:
                    coords[0] -= dirs[cur_dir][0]
                    coords[1] -= dirs[cur_dir][1]
                res = max(res, coords[0] ** 2 + coords[1] ** 2)
            else:
                if step == -1:
                    cur_dir += 1
                elif step == -2:
                    cur_dir -= 1
                cur_dir %= 4

        return res
