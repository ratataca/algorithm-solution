T = int(input())

while T:
    score = input()

    isOK = False
    cnt = 0
    result = 0
    for i in score:
        if i == "O" and isOK == False:
            isOK = True
            cnt += 1
            result += cnt
        elif i == "O" and isOK == True:
            cnt += 1
            result += cnt
        elif i == "X" and isOK == True:
            isOK = False
            cnt = 0

    T -= 1

    print(result)
