class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        rewards: list[tuple[int, int]] = sorted(zip(reward1, reward2), key=lambda rs: -(rs[0] - rs[1]))
        res = 0
        for rew in rewards:
            res += rew[0 if k > 0 else 1]
            k -= 1

        return res
