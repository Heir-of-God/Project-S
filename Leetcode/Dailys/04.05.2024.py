class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        res = 0
        mn_ind: int = 0
        mx_ind: int = len(people) - 1
        people.sort()

        while mn_ind <= mx_ind:
            if people[mx_ind] + people[mn_ind] <= limit:
                mn_ind += 1
            res += 1
            mx_ind -= 1
        return res
