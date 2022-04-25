N = int(input())
arr = []
memo = [0] * (N+1)
for idx in range(N):
    arr.append([int(input()), idx])

stack = []

for value, idx in arr:
    if stack[-1] > value:
        target, target_idx = stack.pop()
    else:
        pass
    stack.append([value, idx])





