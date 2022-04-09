from math import sqrt

def is_prime_num(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime_num(13))
print(is_prime_num(7))
print(is_prime_num(112))


from itertools import permutations, combinations

a = [1, 2, 3, 4, 5]

print(list(permutations(a, 3)))
print(list(permutations(a, 2)))

print("-" * 40)

print(list(combinations(a, 3)))