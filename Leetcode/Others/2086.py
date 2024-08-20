class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if "HHH" in hamsters or "HH" in [hamsters[:2], hamsters[-2:]] or not "." in hamsters:
            return -1
        n: int = len(hamsters)
        cur_ind: int = 0
        last_bucket_ind: int = -5
        last_bucket_feeding: int = 0
        res: int = 0

        while cur_ind < n:
            if hamsters[cur_ind] == ".":
                if "H" in [hamsters[max(0, cur_ind - 1)], hamsters[min(n - 1, cur_ind + 1)]]:
                    if hamsters[max(0, cur_ind - 1)] == "H" and last_bucket_ind != cur_ind - 2:
                        last_bucket_ind = cur_ind
                        res += 1
                        if hamsters[min(n - 1, cur_ind + 1)] == "H":
                            last_bucket_feeding = 2
                            cur_ind += 1
                    elif hamsters[min(n - 1, cur_ind + 1)] == "H":
                        if hamsters[max(0, cur_ind - 1)] == "H" and (
                            last_bucket_ind != cur_ind - 2
                            or (last_bucket_ind == cur_ind - 2 and last_bucket_feeding == 1)
                        ):
                            last_bucket_feeding = 2
                            res -= 1
                        else:
                            last_bucket_feeding = 1
                        last_bucket_ind = cur_ind
                        res += 1

            cur_ind += 1

        return res


# just shock...
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        return (
            -1
            if "HHH" in hamsters or "HH" in [hamsters[:2], hamsters[-2:]] or hamsters == "H"
            else hamsters.count("H") - hamsters.count("H.H")
        )
