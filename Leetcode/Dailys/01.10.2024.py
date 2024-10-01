class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        counter: list[int] = [0 for _ in range(k)]
        for n in arr:
            counter[n % k] += 1

        if counter[0] & 1 == 1:
            return False

        left = 1
        right = k - 1

        while left <= right:
            if counter[left] != counter[right]:
                return False
            left += 1
            right -= 1

        return True
