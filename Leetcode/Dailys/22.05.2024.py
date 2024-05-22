class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res: list[list[str]] = []
        n: int = len(s)

        def is_palindrome(s):
            left: int = 0
            right: int = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        def get_all_partitions(cur_ind, cur_list) -> None:
            is_last_palindrome = is_palindrome(cur_list[-1])
            if cur_ind == n:
                if is_last_palindrome:
                    res.append(cur_list[:])
                return
            if is_last_palindrome:
                cur_list.append(s[cur_ind])
                get_all_partitions(cur_ind + 1, cur_list)
                cur_list.pop()
            cur_list[-1] = cur_list[-1] + s[cur_ind]
            get_all_partitions(cur_ind + 1, cur_list)
            cur_list[-1] = cur_list[-1][:-1]

        get_all_partitions(1, [s[0]])
        return res
