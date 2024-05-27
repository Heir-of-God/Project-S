class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n: int = len(nums)

        def find_number_of_nums(cur_num) -> int:
            left: int = 0
            right: int = n - 1

            first_index: int = n
            while left <= right:
                mid: int = (left + right) // 2

                if nums[mid] >= cur_num:
                    first_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return n - first_index

        for candidate_number in range(1, n + 1, 1):
            if candidate_number == find_number_of_nums(candidate_number):
                return candidate_number

        return -1


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n: int = len(nums)
        frequency: list[int] = [0 for _ in range(n + 1)]  # frequence[i] means there is frequence[i] elements equal to i

        for num in nums:
            frequency[min(n, num)] += 1

        num_greater_equal = 0
        for candidate_number in range(n, 0, -1):
            num_greater_equal += frequency[candidate_number]
            if candidate_number == num_greater_equal:
                return candidate_number

        return -1
