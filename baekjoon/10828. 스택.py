import sys
input = sys.stdin.readline

T = int(input())
stack = []

while T:
    event = input()
    if 'push' in event:
        v = event.split()[1]
        stack.append(v)
        
    elif event == 'pop':
        if len(stack) > 0:
            v = stack.pop()
            print(v)
        else:
            print(-1)

    elif event == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
        
    elif event == 'size':
        print(len(stack))

    elif event == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    T -= 1