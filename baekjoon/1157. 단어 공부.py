"""
인덱스로 접근 할 때는 항상 범위를 고민 할 것!
"""

from collections import defaultdict

text = input().upper()

char_dict = defaultdict(int)

for t in text:
    char_dict[t] += 1

sorted_char = sorted(char_dict.items(), reverse=True, key=lambda i: i[1])

if len(sorted_char) > 1 and sorted_char[0][1] == sorted_char[1][1]:
    print("?")
else:
    print(sorted_char[0][0])