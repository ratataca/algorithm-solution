num = int(input())

for i in range(1, num):
    arr = []
    for s in str(i):
        n = int(s)
        arr.append(n)
    arr.append(i)

    if sum(arr) == num:
        print(i)
        break
else:
    print(0)