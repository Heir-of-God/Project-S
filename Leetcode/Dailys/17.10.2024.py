class Solution:
    def maximumSwap(self, num: int) -> int:
        num: list[str] = list(str(num))
        n: int = len(num)

        max_right: int = int(num[-1])
        max_ind: int = n - 1
        swap1 = swap2 = -1

        for ind in range(n - 2, -1, -1):
            here = int(num[ind])
            if here < max_right:
                swap1 = ind
                swap2 = max_ind

            if here > max_right:
                max_right = here
                max_ind = ind

        if swap1 != -1:
            num[swap1], num[swap2] = num[swap2], num[swap1]

        return int("".join(num))
