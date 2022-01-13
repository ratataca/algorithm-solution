n = input()

mid = len(n) // 2
sum1 = 0
sum2 = 0

for i in range(mid):
    sum1 += int(n[i])
    sum2 += int(n[mid + i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")