from re import I


N = int(input())

result = 0
for i in range(N+1):
    if i % 2 == 0:
        result += i

print(result)