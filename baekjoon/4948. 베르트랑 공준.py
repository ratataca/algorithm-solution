from math import sqrt

prime_num = [True] * (2 * 123456 + 1)
prime_num[0] = prime_num[1] = False

def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':

    for pn in range(len(prime_num)):
        if is_prime_num(pn):
            prime_num[pn] = True
        else:
            prime_num[pn] = False

    while True:
        num = int(input())
        cnt = 0

        if num == 0:
            break

        for i in range(num + 1, 2 * num + 1):
            if prime_num[i]:
                cnt += 1

        print(cnt)