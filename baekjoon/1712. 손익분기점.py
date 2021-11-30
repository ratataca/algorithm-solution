# A : 고정비용
# B : 가변비용
# c : 노트북 가격
A, B, C = [int(n) for n in input().split(" ")]

# result * C >= A + B * result
try:
    result = int(A / (C - B)) + 1

    if result < 1:
        print(-1)
    else:
        print(result)

except ZeroDivisionError:
    print(-1)