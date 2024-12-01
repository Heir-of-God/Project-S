class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        arr = set(arr)
        for el in arr:
            if el != 0 and el * 2 in arr:
                return True
        return False
