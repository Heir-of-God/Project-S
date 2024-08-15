class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        cur_have: list[int] = [0, 0]  # 5 and 10

        for bill in bills:
            if bill == 5:
                cur_have[0] += 1
            elif bill == 10:
                if cur_have[0] == 0:
                    return False
                cur_have[0] -= 1
                cur_have[1] += 1
            elif bill == 20:
                if cur_have[0] > 0 and cur_have[1] > 0:
                    cur_have[0] -= 1
                    cur_have[1] -= 1
                elif cur_have[0] >= 3:
                    cur_have[0] -= 3
                else:
                    return False

        return True
