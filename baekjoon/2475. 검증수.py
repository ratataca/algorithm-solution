num = [int(n) for n in input().split()]

unique_num = 0
for n in num:
    unique_num += (n * n)

print(unique_num % 10)
