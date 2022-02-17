## 10-5) Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.

def sparseSearch(arr, target):
    left, right = 0, len(arr) -1
    while left < right:
        mid = (left + right) // 2

        # 빈 값일 경우 가까운 키워드로 mid 조정
        if not arr[mid]:
            delta = 1
            while not arr[mid+delta] and not arr[mid-delta]:
                delta += 1
            mid = mid+delta if arr[mid+delta] else mid-delta

        if arr[mid] == target:
            return mid

        if arr[mid] < target: 
            left = mid + 1
        else: 
            right = mid
            
    return -1