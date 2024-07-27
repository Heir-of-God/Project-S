class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        res: int = 0
        skip: bool = False
        text += " "

        for char in text:
            if char == " ":
                res += not skip
                skip = False
            if not skip:
                skip = char in broken

        return res
