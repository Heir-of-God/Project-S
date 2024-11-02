class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for ind in range(1, len(words)):
            if words[ind - 1][-1] != words[ind][0]:
                return False

        return sentence[0] == sentence[-1]
