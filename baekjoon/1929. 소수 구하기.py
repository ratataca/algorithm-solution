from math import sqrt

def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

M, N = [int(n) for n in input().split()]

for i in range(M, N+1):
    if is_prime_num(i):
        print(i)