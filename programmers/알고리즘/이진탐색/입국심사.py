def isTimeOk(mid, times):
    count = 0
    for time in times:
        count += (mid // time)
    return count
    
    # print(f"> T: {T}, count: {count}, sum: {sum(count)}")
    return sum(count)
    

def solution(n, times):
    min_value = 1
    max_value = max(times) * n
    # print(f">>> min: {min_value}, max: {max_value}")
    
    while min_value <= max_value:
        mid = int((min_value + max_value) // 2)
        
        print(f"min: {min_value}, max: {max_value}, mid: {mid}")
        if isTimeOk(mid, times) >= n:
            answer = mid
            max_value = mid - 1
        else:   
            min_value = mid + 1
            
    return answer

solution(6, [7, 10])