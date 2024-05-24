class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        n: int = len(words)
        res: int = 0

        letters_count: list[int] = [0 for _ in range(26)]
        for letter in letters:
            ind: int = ord(letter) - 97
            letters_count[ind] += 1

        words_scores: dict[str, int] = {}
        for word in words:
            s = 0
            for char in word:
                ind = ord(char) - 97
                s += score[ind]
            words_scores[word] = s

        def recursion(cur_ind, cur_score) -> None:
            nonlocal res

            if cur_ind == n:
                if cur_score > res:
                    res = cur_score
                return

            can_add_this_word = True
            word: str = words[cur_ind]
            word_count: list[int] = [0 for _ in range(26)]
            for char in word:
                ind: int = ord(char) - 97
                word_count[ind] += 1
                if word_count[ind] > letters_count[ind]:
                    can_add_this_word = False
                    break

            if can_add_this_word:
                for ind in range(26):
                    letters_count[ind] -= word_count[ind]
                recursion(cur_ind + 1, cur_score + words_scores[word])
                for ind in range(26):
                    letters_count[ind] += word_count[ind]
            recursion(cur_ind + 1, cur_score)  # recursion without this word

        recursion(0, 0)
        return res


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        n: int = len(words)
        res: int = 0

        letters_count: list[int] = [0 for _ in range(26)]
        for letter in letters:
            ind = ord(letter) - 97
            letters_count[ind] += 1

        words_scores: dict[str, int] = {}
        for word in words:
            s = 0
            for char in word:
                ind: int = ord(char) - 97
                s += score[ind]
            words_scores[word] = s

        for mask in range(0, 2**n, 1):
            cur_count: list[int] = [0 for _ in range(26)]
            can_create = True
            cur_score = 0

            for word_ind in range(n):
                if (mask & (1 << word_ind)) != 0:  # if in mask bit of this word is 1
                    word: str = words[word_ind]
                    cur_score += words_scores[word]
                    for char in word:
                        ind = ord(char) - 97
                        cur_count[ind] += 1
                        if cur_count[ind] > letters_count[ind]:
                            can_create = False
                            break
                if not can_create:
                    break
            if can_create and cur_score > res:
                res = cur_score

        return res
