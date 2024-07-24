import os


def isValid(s: str) -> str:
    freq: list[int] = [0 for _ in range(26)]
    for char in s:
        freq[ord(char) - ord("a")] += 1

    freq_of_frequency: dict[int, int] = {}
    for num in freq:
        if num != 0:
            freq_of_frequency[num] = freq_of_frequency.get(num, 0) + 1

    if len(freq_of_frequency) == 1:
        return "YES"
    elif len(freq_of_frequency) == 2:
        freq1, freq2 = tuple(freq_of_frequency.keys())
        if (freq_of_frequency[freq1] == 1 and (freq1 - 1 == freq2 or freq1 == 1)) or (
            freq_of_frequency[freq2] == 1 and (freq2 - 1 == freq1 or freq2 == 1)
        ):
            return "YES"

    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = isValid(s)
    fptr.write(result + "\n")
    fptr.close()
