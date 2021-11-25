T = int(input())

for t in range(T):
    R, S = [n for n in input().split()]
    text = ""

    for i in S:
        text += i * int(R)

    print(text)