## 8-3 ) Magic Index: A magic index in an array A[e... n-1] is defined to be an index such that A[ i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# 정렬되어있고 같은원소가 아니라는 것이 관건

def solution(n, arr):
    return getMagicIdx(arr)

def getMagicIdx(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return getMagicIdx(arr[:mid])
    else:
        return getMagicIdx(arr[mid+1:])

# 같은 원소가 있을때는 brute force한 방법밖엔 모르겠음
def getMagicIdx(n, arr):
    for i in range(n):
        if arr[i] == i:
            return i
    return None
