class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counter: dict[int, int] = {}
        unique: list[int] = []
        for num in nums:
            if num not in counter:
                unique.append(num)
                counter[num] = 0
            counter[num] += 1

        unique.sort()
        n: int = len(unique)
        dp: list[int] = [0 for _ in range(n + 1)]  # dp[k] -> max for first k elements
        dp[0] = 0
        dp[1] = unique[0] * counter[unique[0]]

        for number_of_numbers in range(2, n + 1, 1):
            cur_number = unique[number_of_numbers - 1]
            prev_num = unique[number_of_numbers - 2]

            if cur_number - prev_num != 1:
                dp[number_of_numbers] = dp[number_of_numbers - 1] + cur_number * counter[cur_number]
            else:
                dp[number_of_numbers] = max(
                    dp[number_of_numbers - 1], dp[number_of_numbers - 2] + cur_number * counter[cur_number]
                )

        return dp[n]


# O(n log n) / O(n) I believe, but too messy and long


# O(n) way more elegant


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        frequency: list[int] = [0 for _ in range(max(nums) + 1)]
        for num in nums:
            frequency[num] += 1

        prev_mx: int = 0
        prev_prev_mx: int = 0

        for number, freq in enumerate(frequency):
            cur: int = max(prev_prev_mx + number * freq, prev_mx)  # maximum among pick / not pick
            prev_mx, prev_prev_mx = cur, prev_mx

        return prev_mx
