# Chapter1. Arrays and Strings

## 1-1 ) Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

```python
def getIsUniqueCharacters(st):
    ST_LEN = len(st)
    # 정렬 사용 -> O(nlogn)
    st = sorted(st)
    for i in range(ST_LEN-1):
        cur, nxt = i, i+1
        if (st[cur] == st[nxt]):
            return False
    return True
```
<hr>

## 1-2 ) Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

```python
def CheckPermutation(str1, srt2):
    char_table = {}
    # hash 이용
    for char in str1:
        char_table[char] = char_table.get(char, 0) + 1
    for char in srt2:
        char_table[char] -= char_table.get(char, 0) - 1
    return not any(char_table.values())
```
<hr>

## 1-3 ) URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

```python
# 문제의도를 잘 이해 못해서 품
import re
def URLify(st):
    result = st.strip()
    return re.sub('\s','\%20', result)
```
<hr>

## 1-4 ) Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.

```python
def isPalindromePermutation(st):
    check_set = set()
    for char in st:
        if char in check_set:
            check_set.remove(char)
        else:
            check_set.add(char)
    return len(check_set) <= 1;
```
<hr>

## 1-5 ) One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

```python
def isUnderOneEdit(str1, srt2):
    len1, len2 = len(str1), len(srt2)
    ge_str1, ge_str2 = len1 >= len2, len2 >= len1 # 캐싱

    if abs(len1 - len2) > 1:
        return False

    pos_cnt = 1 # 수정 가능 횟수
    i, j = 0, 0
    while i < len1 and j < len2:
        if str1[i] != srt2[j] 
            if pos_cnt == 0:
                return False
            pos_cnt -= 1
            i = i+1 if ge_str1 else i
            j = j+1 if ge_str2 else j
        else:
            i, j = i+1, j+1
 
    if i < len1 or j < len2:
        pos_cnt -= 1
 
    return pos_cnt >= 0
```
<hr>

## 1-6 ) String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

```python
# ? lowercase 제한 조건으로 더 좋은 방법이 없을까

def getCompressed(st):
    # 문제에서 string이 없는경우 언급이 없음 - 일단 예외처리
    if st == '':
        return ''

    stack, cnt_arr = [st[0]], [1]
    for char in st[1:]:
        if stack[-1] == char:
            cnt_arr[-1] += 1
        else:
            stack.append(char)
            cnt_arr.append(1)

    compressed = ''.join([char + str(cnt) for char, cnt in zip(stack, cnt_arr)])
    
    return compressed if len(compressed) < len(st) else st
```
<hr>

## 1-7 ) Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

```python
# ? 어느 방향으로 90도 - 시계방향이라 가정
# ? (Can you do this in place) -> 무슨뜻인지 모르겠음
def rotate90(matrix):
    return list(zip(*matrix[::-1]))
```
<hr>

## 1-8 ) Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.

```python
def getZeroMatrix(matrix):
    zero_row, zero_col = set(), set()
    row_len, col_len = len(matrix), len(matrix[0])

    for i in range(row_len):
        for j in range (col_len):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
    for y in zero_row:
        matrix[y] = [0] * col_len
            
    for x in zero_col:
        for j in range(row_len):
            matrix[j][x] = 0

    return matrix

```
<hr>

## 1-9 ) String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one call to isSubstring (e.g.,"waterbottle"is a rotation of "erbottlewat").

```python
import re
# rotation 형태 -> 보통 이어 붙이면 접근 쉬움 
def isSubstring(str1, str2):
    return len(str1) == len(str2) and bool(re.search(str2, str1*2))
```
<hr>
<hr>
<hr>