
cnt = 0
target = int(input())
num = target

while True:

    if num < 10:
        num *= 10

    ten, digit =  num // 10, num % 10
    print("ten: {0}, digit: {1}".format(ten, digit))

    tmp = (ten + digit) % 10
    num = digit * 10 + tmp
    print("tmp: {0}, num: {1}".format(tmp, num))
    cnt += 1

    if target == num:
        break

    print(num)

print(">>>", cnt)
