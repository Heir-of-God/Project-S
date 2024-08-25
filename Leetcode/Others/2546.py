class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s != target and (not "1" in s or not "1" in target):
            return False
        return True
