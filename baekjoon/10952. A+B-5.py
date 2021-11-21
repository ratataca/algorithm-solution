while True:
    num1, num2 = [int(n) for n in input().split(" ")]
    if num1 == 0 and num2 == 0:
        break
    print(num1 + num2)