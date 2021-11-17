num1, num2 = [int(n) for n in input().split(" ")]

if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
else:
    print("==")