x, y = [int(input()) for _ in range(2)]

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)