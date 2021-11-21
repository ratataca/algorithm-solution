T = int(input())

for _ in range(T):
    N = int(input())

    # Memorization
    m = [0] * (N + 1)

    count0, count1 = 0, 0

    if N == 0:
        m[0] = 0
    else:
        m[0], m[1] = 0, 1


    def fibonacci(n):
        global count0, count1

        if n == 0:
            count0 += 1
            return 0

        if n == 1:
            count1 += 1
            return 1

        for i in range(2, n + 1):
            if m[i] == 0:
                m[i] = m[i - 1] + m[i - 2]

        return m[n]


    print(fibonacci(N))