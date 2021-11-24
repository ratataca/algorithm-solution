remainder = set()

for i in range(10):
    num = int(input())
    result = num % 42
    remainder.add(result)

print(len(remainder))