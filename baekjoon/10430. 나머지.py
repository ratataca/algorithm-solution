num1, num2 = [input() for _ in range(2)]
arr = []

for i in range(len(num2) - 1, -1, -1):
    calc = int(num1) * int(num2[i])

    if((2 - i) > 0):
        arr.append(calc * 10** (2 - i))
    else:
        arr.append(calc)
    print(calc)

print(sum(arr))