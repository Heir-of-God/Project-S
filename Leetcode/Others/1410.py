class Solution:
    def entityParser(self, text: str) -> str:
        tags: dict[str, str] = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        text += "&"
        cur_tag_length: int = 0
        cur_tag_start_ind: int = -1
        res: str = ""

        for ind, char in enumerate(text):
            if char == "&":
                if cur_tag_start_ind != -1:
                    cur_tag_length = 0
                    res += text[cur_tag_start_ind:ind]
                cur_tag_start_ind = ind

            if cur_tag_start_ind != -1:
                cur_tag_length += 1
                if cur_tag_length > 7:
                    cur_tag_length = 0
                    res += text[cur_tag_start_ind:ind]
                    cur_tag_start_ind = -1

            if cur_tag_start_ind == -1:
                res += char
            else:
                if text[cur_tag_start_ind : ind + 1] in tags:
                    res += tags[text[cur_tag_start_ind : ind + 1]]
                    cur_tag_start_ind = -1
                    cur_tag_length = 0

        return res
