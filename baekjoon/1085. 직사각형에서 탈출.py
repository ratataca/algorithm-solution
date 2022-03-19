x, y, w, h = [int(n) for n in input().split()]

x_gap = w - x
y_gap = h - y

print(min(x_gap, y_gap, x, y))