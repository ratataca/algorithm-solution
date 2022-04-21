def measure_the_distance(rocks, target):
    remove = 0
    prev_rock = 0
    min_gap = int(1e9) 
    
    for rock in rocks:
        cur_gap = rock - prev_rock
        if cur_gap < target:
            remove += 1
        else:
            min_gap = min(min_gap, cur_gap) 
            prev_rock = rock
        
    return [remove, min_gap]
    
    

def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    min_value = 0
    max_value = distance
    
    while min_value <= max_value:
        mid = (min_value + max_value) // 2
        
        remove, gap = measure_the_distance(rocks, mid)
        if remove > n:
            max_value = mid - 1
        else:
            min_value = mid + 1    
    
    return max_value 
