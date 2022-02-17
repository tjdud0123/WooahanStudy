## 10-10) Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations.That is, implement the method track (in t x), which is called when each number is generated, and the method getRankOfNumber(int x) , which returns the number of values less than or equal to X (not including x itself).

# 방법 1
# O(nlogn) / O(logn)
from bisect import bisect_right

arr = [1, 4, 4, 5, 9, 7, 13, 3]
arr.sort()

def getRankOfNumber(arr, target):
    # bisect로 이분탐색
    r_idx = bisect_right(arr, target)
    return r_idx if r_idx == len(arr) else r_idx - 1

print(getRankOfNumber(arr, 4)) # 3
print(getRankOfNumber(arr, 3)) # 1 
print(getRankOfNumber(arr, 1)) # 0
print(getRankOfNumber(arr, 15)) # 8

# 방법 2 - 숫자간격이 작으면 유리, 탐색이 잦을 때
# O(n2) / O(1)

# {1: 0, 2: 1, 3: 1, 4: 3, 5: 4, 6: 5, 7: 5, 8: 6, 9: 6, 10: 7, 11: 7, 12: 7, 13: 7}
def getRankOfNumber2(table, target, max_val, min_val):
    if max_val < target:
        return len(arr)
    elif target < min_val:
        return 0
    else:
        return table[target]

def getTable(arr, max_val, min_val):
    table = {}
    prev = max_val
    for num in arr:
        for key in table:
            table[key] += 1
        if num not in table:
            table[num] = 0
        # 없는 숫자 채워주기
        for blank_i in range(prev - 1, num, -1):
            table[blank_i] = table[prev]
        prev = num
            
    return table

arr = [1, 4, 4, 5, 9, 7, 13, 3]
arr.sort(reverse=True)
max_val, min_val = max(arr), min(arr)
arr_len = len(arr)
table = getTable(arr, max_val, min_val)

print(getRankOfNumber2(table, 4, max_val, min_val)) # 3
print(getRankOfNumber2(table, 3, max_val, min_val)) # 1 
print(getRankOfNumber2(table, 1, max_val, min_val)) # 0
print(getRankOfNumber2(table, 15, max_val, min_val)) # 8