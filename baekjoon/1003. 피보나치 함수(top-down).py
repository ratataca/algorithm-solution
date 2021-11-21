import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    count0, count1 = 0, 0
    m = [0] * (N + 1)

    def fibonacci(n):
        global count0, count1

        if n == 0:
            count0 += 1
            return 0

        elif n == 1:
            count1 += 1
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

        # if m[n] == 0:
        #     m[n] = fibonacci(n - 1) + fibonacci(n - 2)
        #
        #     return m[n]
        # else:
        #     return m[n]

    fibonacci(N)
    print(count0, count1)


# N = int(input())
#
# for _ in range(N):
#     num = int(input())
#
#     m = [[0] * 3] * (num + 1)
#
#     def fibonacci(n):
#         if n == 0:
#             return [0, 1, 0]
#         elif n == 1:
#             return [1, 0, 1]
#         elif m[n][0] != 0:
#             return m[n]
#         else:
#             f1, f10, f11 = fibonacci(n - 1)
#             f2, f20, f21 = fibonacci(n - 2)
#
#             m[n] = [f1 + f2, f10 + f20, f11 + f21]
#             return m[n]
#
#     _, count0, count1 = fibonacci(num)
#     print(count0, count1)