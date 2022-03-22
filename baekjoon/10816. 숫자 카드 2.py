'''
이분 탐색의 경우 구간의 중간 위치의 값과 
key(찾고자 하는 값)를 비교하여 구간을 절반으로 줄여나가며 풀이.

'''

from collections import defaultdict

N = int(input())
cards = [int(n) for n in input().split()]

M = int(input())
check_cards = [int(n) for n in input().split()]
m_dict = defaultdict(int)

for key in check_cards:
    m_dict[key] = 0

for card in cards:
    if card in m_dict.keys():
        m_dict[card] = m_dict[card] + 1
        
print(' '.join([str(m_dict[ck]) for ck in check_cards]))


