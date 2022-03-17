
while True:
    num = input()
    if num == 0:
        break

    if num[0:len(num)/2] == num[len(num)/2:-1:-1]:
        print('yes', num[0:len(num)/2])
    else:
        print("no")
    

    
