n = int(input())

while n >0:
    num1, num2 = [int(n) for n in input().split()]
    print(num1 + num2)
    n -= 1