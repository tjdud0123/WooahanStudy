## 10-4) Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size method.It does, however, have an elementAt(i) method that returns the element at index i in 0(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.

def search(arr, target):
    idx = 1
    cur_el = arr.elementAt[idx]
    while cur_el != -1 and cur_el < val:
        idx *= 2
    return binarySearch(arr, target, idx // 2, idx)

def binarySearch(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        mid_el = arr.elementAt[mid]
        if mid_el > target or mid_el == -1:
            right = mid - 1
        elif mid_el < target:
            left = mid + 1
        else:
            return mid

    return -1