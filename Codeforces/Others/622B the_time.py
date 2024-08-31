hours, minutes = [int(i) for i in input().split(":")]
add = int(input())
total_time = (hours * 60 + minutes + add) % (24 * 60)
hours = str(total_time // 60).zfill(2)
minutes = str(total_time % 60).zfill(2)

print(f"{hours}:{minutes}")
