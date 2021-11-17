h, m = [int(n) for n in input().split()]

before_time = h * 60 + m
before_time = before_time - 45

before_h = before_time // 60
before_m = before_time % 60

if before_h < 0:
    before_h = 24 + before_h

print(before_h, before_m)