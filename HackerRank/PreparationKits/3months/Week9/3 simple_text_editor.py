import os


class TextEditor:
    def __init__(self) -> None:
        self.cur_state: list[str] = []
        self.history: list[str] = []

    def add_str(self, string: str) -> None:
        chars = list(string)
        self.history.append(self.cur_state[:])
        self.cur_state += chars

    def delete_chars(self, how_many: int) -> None:
        self.history.append(self.cur_state[:])
        self.cur_state = self.cur_state[: len(self.cur_state) - how_many]

    def print_k(self, k: int) -> None:
        fptr.write(self.cur_state[k - 1] + "\n")

    def undo(self) -> None:
        self.cur_state = self.history.pop()


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    editor = TextEditor()

    for _ in range(t):
        inp = input()
        if inp[0] == "1":
            op, val = inp.split(maxsplit=1)
            editor.add_str(val)
        elif inp[0] == "2":
            op, val = inp.split(maxsplit=1)
            val = int(val)
            editor.delete_chars(val)
        elif inp[0] == "3":
            op, val = inp.split(maxsplit=1)
            val = int(val)
            editor.print_k(val)
        elif inp[0] == "4":
            editor.undo()

    fptr.close()
