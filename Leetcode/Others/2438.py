class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        powers_of_two: list[int] = []
        power = 0
        while 2**power <= n:
            powers_of_two.append(2**power)
            power += 1
        powers_of_two.reverse()

        powers: list[int] = []
        cur_ind = 0
        while n != 0:
            add: int = n // powers_of_two[cur_ind]
            n -= add * powers_of_two[cur_ind]
            for _ in range(add):
                powers.append(powers_of_two[cur_ind])
            cur_ind += 1
        powers.reverse()

        prefix_prod: list[int] = [1] + [powers[0]]
        for ind in range(1, len(powers), 1):
            prefix_prod.append((prefix_prod[-1] * powers[ind]))

        res: list[int] = []
        for left, right in queries:
            res.append((prefix_prod[right + 1] // prefix_prod[left]) % MOD)

        return res
