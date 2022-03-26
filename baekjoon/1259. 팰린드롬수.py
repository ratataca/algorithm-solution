
while True:
    num = input()
    if num == '0':
        break

    if len(num) % 2 == 0:
        target = int(len(num) / 2)
        if num[ : target] == num[len(num) : target-1 : -1]:
            print('yes')
        else:
            print("no")
    else:
        target = int(len(num) / 2)
        if num[ : target] == num[len(num) : target : -1]:
            print('yes')
        else:
            print("no")
