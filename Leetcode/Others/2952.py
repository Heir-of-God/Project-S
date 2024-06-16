class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()
        res: int = 0
        cur_max_ending: int = 0
        cur_ind: int = 0

        while cur_max_ending < target:
            if cur_ind < len(coins) and coins[cur_ind] <= cur_max_ending + 1:
                cur_max_ending += coins[cur_ind]
                cur_ind += 1
            else:
                cur_max_ending += cur_max_ending + 1
                res += 1

        return res


# The same as https://leetcode.com/problems/patching-array/description/
