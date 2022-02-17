## 10-3) Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

from bisect import bisect_left

# rotate 지점 찾기
def getRotatePoint(left, right, arr):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1;
        else:
            right = mid
    return left

def searchTarget(arr, target):
    left, right = 0, len(arr)-1
    rotate_point = getRotatePoint(left, right, arr)
    sorted_arr = arr[rotate_point:] + arr[:rotate_point]
    # bisect로 이분탐색
    l_idx = bisect_left(sorted_arr, target)
    return l_idx if arr[l_idx] == target else -1