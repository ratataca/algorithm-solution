'''
# 이진 검색을 적용하기 전에 항상 먼저 정렬

1. 사전 처리 - 컬렉션이 정렬되지 않은 경우 정렬합니다.
2. 이진 검색 - 루프 또는 재귀를 사용하여 각 비교 후 검색 공간을 반으로 나눕니다.
3. 후처리 - 남은 공간에서 실행 가능한 후보를 결정합니다.


Target - 찾고 있는 값
Index  - 검색 중인 현재 위치
Left, Right - 검색 공간을 유지 관리하는 데 사용하는 인덱스
Mid - 왼쪽 또는 오른쪽 검색 여부를 결정하기 위해 조건을 적용하는 데 사용하는 인덱스
'''

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


from collections import defaultdict

N = int(input())
cards = [int(n) for n in input().split()]

M = int(input())
check_cards = [int(n) for n in input().split()]







print(' '.join([str(m_dict[ck]) for ck in check_cards]))


