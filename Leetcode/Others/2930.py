class Solution:
    def stringCount(self, n: int) -> int:
        if n <= 3:
            return 0
        MOD = 10**9 + 7
        total = (26**n) % MOD

        bad_strings = 0
        # there no l
        bad_strings += (25**n) % MOD
        # there no t
        bad_strings += (25**n) % MOD
        # there no e
        bad_strings += (25**n) % MOD
        # there only 1 e
        bad_strings += n * (25 ** (n - 1)) % MOD

        # Now we counted several times cases with no l, t and e in [0, 1], we need to reduce their count

        # no l and no t
        bad_strings -= (24**n) % MOD
        # l = 0, e < 2
        bad_strings -= (24**n) % MOD + n * (24 ** (n - 1)) % MOD
        # t = 0, e < 2
        bad_strings -= (24**n) % MOD + n * (24 ** (n - 1)) % MOD
        # l = 0, t = 0, e < 2 (we deleted this case while reducing number of bad strings)
        bad_strings += (23**n) % MOD + n * (23 ** (n - 1)) % MOD

        return (total - bad_strings) % MOD
