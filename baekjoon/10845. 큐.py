from collections import deque
import sys
input = sys.stdin.readline

q = deque([])
T = int(input())

while T > 0:
    command = input().split()

    if "push" == command[0]:
        x = command[1]
        q.append(x)

    elif "pop" == command[0]:
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif "size" == command[0]:
        print(len(q))
    elif "empty" == command[0]:
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif "front" == command[0]:
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif "back" == command[0]:
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)

    T -= 1