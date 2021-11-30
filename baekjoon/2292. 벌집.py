# 1  1
# 6  2-7
# 12 8-19
# 18 20-37
# 24 38-61

find_num = int(input())
category = 0

num1 = 0
num2 = 1

while True:
    if num1 <= find_num and find_num <= num2:
        break

    category += 1
    num1 = num2 + 1
    num2 = num2 + 6*category


print(category+1)