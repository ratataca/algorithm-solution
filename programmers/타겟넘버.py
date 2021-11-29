def solution(numbers, target):
    dfs_visited = [False] * len(numbers)
    index = [n for n in range(len(numbers))]
    stack = [index[0]]

    while stack:
        V = stack.pop()


        for i in range(len(numbers[V] -1), -1, -1):
            stack.append(i+1)
            stack.append(i-1)

number = [1, 1, 1, 1, 1]
target = 3
solution(number, target)