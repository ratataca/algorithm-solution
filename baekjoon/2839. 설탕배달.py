KG_5 = 5
KG_3 = 3

num = int(input())
arr = []

target_1 = num // KG_5 + 1
target_2 = num // KG_3 + 1
for i in range(target_1):
    for j in range(target_2):
        if (KG_5 * i) + (KG_3 * j) == num:
            arr.append(i + j)

if len(arr) > 0:
    print(min(arr))
else:
    print(-1)