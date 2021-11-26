# Sol 1
N = int(input())
result = []

for i in range(2, N+1):
    while True:
        if N % i == 0:
            N = N // i
            print(i)
        else:
            break


# Sol 2
# N = int(input())
# prime_numbers = [2, 3, 5, 7, 11]
#
# while N != 1:
#     i = 2
#     while True:
#         if N % i == 0:
#             N = N // i
#             print(i)
#             break
#
#         i += 1