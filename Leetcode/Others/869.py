class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_length_and_counter(num) -> tuple[int, dict[int, int]]:
            res = 0
            counter: dict[int, int] = {}

            while num > 0:
                res += 1
                dig: int = num % 10
                if dig not in counter:
                    counter[dig] = 0
                counter[dig] += 1
                num //= 10

            return (res, counter)

        length, src_counter = get_length_and_counter(n)
        powers_of_two: list[dict[int, int]] = [] if length != 1 else [{1: 1}]
        cur = 1

        while True:
            cur *= 2
            l, c = get_length_and_counter(cur)
            if l > length:
                break
            elif l == length:
                powers_of_two.append(c)

        for cnt in powers_of_two:
            if cnt == src_counter:
                return True

        return False
