class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        n: int = len(seats)
        seats.sort()
        students.sort()
        res: int = 0

        for ind in range(n):
            res += abs(seats[ind] - students[ind])

        return res
