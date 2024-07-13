class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n: int = len(positions)
        robots: list[list] = [[positions[ind], healths[ind], directions[ind], ind] for ind in range(n)]
        robots.sort()
        stack: list[list] = []

        for robot in robots:
            if robot[2] == "R" or not stack or stack[-1][2] == "L":
                stack.append(robot)
                continue

            if robot[2] == "L":
                add = True
                while stack and stack[-1][2] == "R" and add:
                    last_health: int = stack[-1][1]
                    if robot[1] > last_health:
                        stack.pop()
                        robot[1] -= 1
                    elif robot[1] < last_health:
                        stack[-1][1] -= 1
                        add = False
                    else:
                        stack.pop()
                        add = False

                if add:
                    stack.append(robot)

        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]
