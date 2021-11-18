t = int(input())

for i in range(1, t + 1):
    for j in range(t - i, 0, -1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()