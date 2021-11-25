dial = {
    "ABC": 3,
    "DEF": 4,
    "GHI": 5,
    "JKL": 6,
    "MNO": 7,
    "PQRS": 8,
    "TUV": 9,
    "WXYZ": 10,
}

text = input()

wait_time = 0
for t in text:
    for i, v in dial.items():
        if t in i:
            wait_time += v

print(wait_time)