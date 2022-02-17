## 10-1) Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order

def merge(arr_A, arr_B):
    LEN_A, LEN_B = len(arr_A), len(arr_B)
    a_idx, b_idx = LEN_A - 1, LEN_B - 1
    merged_idx = LEN_A + LEN_B - 1
    while b_idx > 0:
        # B 남은 원소들이 A 첫원소보다 작을 때
        if a_idx < 0:
            arr_A[:merged_idx+1] = arr_B[:b_idx+1]
            break
        # A 원소가 더 큰경우 
        if arr_A[a_idx] > arr_B[b_idx]:
            arr_A[merged_idx] = arr_A[a_idx]
            a_idx -= 1
        # B 원소가 더 큰경우
        else:
            arr_A[merged_idx] = arr_B[b_idx]
            b_idx -= 1

        merged_idx -= 1
    return arr_A