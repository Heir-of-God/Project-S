class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        curr_diff = 0
        res = 0

        for ind in range(len(gas)):
            curr_diff += gas[ind] - cost[ind]

            if curr_diff < 0:
                curr_diff = 0
                res: int = ind + 1

        return res
