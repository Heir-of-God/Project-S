class KthLargest:

    def __init__(self, k: int, nums: list[int]) -> None:
        self.k: int = k
        self.nums: list[int] = nums
        self.nums = sorted(self.nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.nums) == self.k and self.nums[-1] >= val:
            return self.nums[self.k - 1]
        ind = 0
        while ind < len(self.nums) and self.nums[ind] > val:
            ind += 1
        self.nums = self.nums[:ind] + [val] + self.nums[ind:]
        self.nums = self.nums[: self.k]

        return self.nums[self.k - 1]


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k: int = k
        self.nums = nums
        heapq.heapify(nums)
        self.delete_extra()

    def delete_extra(self):
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self.delete_extra()

        return self.nums[0]
