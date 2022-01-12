from collections import defaultdict

def solution(phone_book):
    hash_map = defaultdict()

    for pb in phone_book:
        hash_map[pb] = 1

    for pb in hash_map.keys():
        text = ""
        for p in pb:
            text += p
            if text != pb:
                return False
    return True