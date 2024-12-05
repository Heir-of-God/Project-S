class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n: int = len(start)
        cur_in_target: int = 0
        cur_in_start: int = 0
        target_char: str = "_"
        start_char: str = "_"

        while cur_in_target < n or cur_in_start < n:
            if (
                target_char != start_char
                or (target_char == "R" and cur_in_start > cur_in_target)
                or (target_char == "L" and cur_in_start < cur_in_target)
            ):
                return False

            while cur_in_target < n and target[cur_in_target] == "_":
                cur_in_target += 1
            target_char = target[cur_in_target] if cur_in_target < n else "_"
            cur_in_target += 1

            while cur_in_start < n and start[cur_in_start] == "_":
                cur_in_start += 1
            start_char = start[cur_in_start] if cur_in_start < n else "_"
            cur_in_start += 1

        return target_char == start_char
