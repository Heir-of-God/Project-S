class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        n: int = len(robot)
        factory.sort()
        temp: list[int] = []
        for pos, num in factory:
            temp += [pos] * num
        factory = temp
        m: int = len(factory)

        memo: list[list[int]] = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        for ind in range(n + 1):  # for any ind on robots if we don't have stations
            memo[ind][m] = 1e12
        for ind in range(m + 1):
            memo[n][ind] = 0

        def recursion(robot_ind, factory_ind):
            if memo[robot_ind][factory_ind] == -1:
                choose = abs(factory[factory_ind] - robot[robot_ind]) + recursion(robot_ind + 1, factory_ind + 1)
                not_choose = recursion(robot_ind, factory_ind + 1)
                memo[robot_ind][factory_ind] = min(choose, not_choose)

            return memo[robot_ind][factory_ind]

        recursion(0, 0)
        return memo[0][0]
