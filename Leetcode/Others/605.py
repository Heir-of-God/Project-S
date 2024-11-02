class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        for ind in range(len(flowerbed)):
            if flowerbed[ind] == 0:
                left: bool = (ind == 0) or (flowerbed[ind - 1] == 0)
                right: bool = (ind == len(flowerbed) - 1) or (flowerbed[ind + 1] == 0)

                if left and right:
                    n -= 1
                    if n == 0:
                        return True
                    flowerbed[ind] = 1

        return False
