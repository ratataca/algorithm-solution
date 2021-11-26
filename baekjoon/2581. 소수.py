from math import sqrt

def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


M = int(input())
N = int(input())

sum_num = 0
min_num = 10000

for i in range(M, N+1):
    if is_prime_num(i):
        sum_num += i
        if min_num > i:
            min_num = i

if sum_num > 0:
    print("{0} {1}".format(sum_num, min_num))
else:
    print(-1)