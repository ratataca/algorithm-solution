t = int(input())

for i in range(1, t + 1):
    num1, num2 = [int(n) for n in input().split(" ")]
    print("Case #{0}: {1} + {2} = {3}".format(i, num1, num2, num1+num2))