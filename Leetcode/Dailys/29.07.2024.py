class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n: int = len(rating)
        res = 0
        for midle_ind in range(n):
            # forgot about uniqueness
            bigger_left = 0
            smaller_left = 0
            bigger_right = 0
            smaller_right = 0
            midle: int = rating[midle_ind]

            for ind in range(midle_ind):
                if rating[ind] < midle:
                    smaller_left += 1
                elif rating[ind] > midle:
                    bigger_left += 1

            for ind in range(midle_ind + 1, n):
                if rating[ind] < midle:
                    smaller_right += 1
                elif rating[ind] > midle:
                    bigger_right += 1

            res += smaller_left * bigger_right
            res += bigger_left * smaller_right

        return res
