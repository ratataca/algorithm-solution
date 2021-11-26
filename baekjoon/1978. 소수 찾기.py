from math import sqrt


def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


T = int(input())
arr = [int(n) for n in input().split()]

cnt = 0

for a in arr:
    if is_prime_num(a):
        cnt += 1

print(cnt)