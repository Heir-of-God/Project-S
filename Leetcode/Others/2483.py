class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers += "_"  # character to consider closing after last hour
        n: int = len(customers)
        cur_y: int = customers.count("Y")
        cur_n: int = 0
        min_penalty: int = float("inf")
        res: int = -1

        for hour in range(n):
            cur_penalty: int = cur_y + cur_n
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                res = hour

            if customers[hour] == "Y":
                cur_y -= 1
            else:
                cur_n += 1

        return res
