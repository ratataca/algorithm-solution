max_idx, max_num = -1, -1

for i in range(9):
    target = int(input())
    if target > max_num:
        max_idx = i + 1
        max_num = target

print("{0}\n{1}".format(max_num, max_idx))
