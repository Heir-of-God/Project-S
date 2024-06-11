import os


def to_seconds(s) -> int:
    hours_sec: int = int(s[:2]) * 3600
    minutes_sec: int = int(s[3:5]) * 60
    return hours_sec + minutes_sec + int(s[6:8])


def timeConversion(s: str) -> str:
    ext: str = s[-2:]
    seconds: int = to_seconds(s[:-2])
    if ext == "AM":
        seconds = seconds if seconds < 12 * 3600 else seconds - 12 * 3600
    elif ext == "PM":
        seconds = seconds if seconds > 12 * 3600 else seconds + 12 * 3600

    h: int = seconds // 3600
    seconds -= h * 3600
    m: int = seconds // 60
    secs: int = seconds % 60
    return f"{str(h):>02}:{str(m):>02}:{str(secs):>02}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = timeConversion(s)
    fptr.write(result + "\n")
    fptr.close()
