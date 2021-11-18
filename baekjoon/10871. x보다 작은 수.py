_, target = [int(n) for n in input().split(" ")]
[print(n, end=" ") for n in input().split(" ") if int(n) < target]
