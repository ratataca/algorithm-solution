"""
baabaa

t = [b]
t = [b, a]
t = [b, a, a]
t = [b, c, c]

for s in 

"""
def solution(S): 
    stack = []
    for value in S:
        stack.append(value)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    if len(stack):
        return 0
    return 1


S = "baabaa"
S = "cdcd"
S = "bcaabccdbd"
print(solution(S))