matrix_num = [0] * 10

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = str(num1 * num2 * num3)
for s in result:
    matrix_num[int(s)] += 1

for i in matrix_num:
    print(i)