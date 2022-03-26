N = int(input())
cnt = 0
num = 0
while True:
    num += 1
    if '666' in str(num):
        cnt += 1
        if N == cnt:
            break

print(num)