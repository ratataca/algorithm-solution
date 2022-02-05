def dfs(start_node, computers, visited):
    stack = [start_node]

    while stack:
        # O(1)
        s = stack.pop()

        for x, _ in enumerate(computers[s]):
            if visited[x] == False and computers[s][x] == 1:
                stack.append(x)
                visited[x] = True


def solution(n, computers):
    answer = 1
    visited = [False] * n
    start_node = 0
    visited[0] = True

    while True:
        dfs(start_node, computers, visited)
        if False not in visited:
            break
        else:
            start_node = visited.index(False)
            answer += 1

    return answer
