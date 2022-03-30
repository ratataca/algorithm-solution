up, down, target = map(int, input().split())

day = (target - down) / (up - down)
print(int(day) if day == int(day) else int(day) + 1)