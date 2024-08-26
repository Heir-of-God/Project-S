class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        n: int = len(sentence)

        for ind in range(n):
            word: str = sentence[ind]
            if word.startswith("$") and word[1:].isdigit():
                price: float = int(word[1:]) * (1 - (discount / 100))
                sentence[ind] = f"${price:.2f}"

        return " ".join(sentence)
