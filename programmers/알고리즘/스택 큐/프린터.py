def solution(priorities, location):
    answer = 0
    items = [(pri, idx) for idx, pri in enumerate(priorities)]

    while True:
        if len(items) == 0:
            break         
        item = items[0]
        if max(items)[0] == item[0]:
            answer += 1
            if item[1] == location:
                return answer
        else:
            items.append(item)

        items.pop(0)
    return answer
