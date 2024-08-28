class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words: list[str] = title.split()
        for ind in range(len(words)):
            words[ind] = words[ind].capitalize()
            if len(words[ind]) <= 2:
                words[ind] = words[ind].lower()

        return " ".join(words)
