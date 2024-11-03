class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n: int = len(s)

        def check_from_ind(start: int) -> bool:
            goal_ind = 0
            for ind in range(start, start + n, 1):
                ind %= n
                if s[ind] != goal[goal_ind]:
                    return False
                goal_ind += 1

            return True

        for ind in range(n):
            if s[ind] == goal[0]:
                if check_from_ind(ind):
                    return True

        return False


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s * 2
