line = input()
instr = input()

line_ind = 0

for i in instr:
    if line[line_ind] == i:
        line_ind += 1

print(line_ind + 1)
