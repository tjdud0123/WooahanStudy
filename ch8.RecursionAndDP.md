# Chapter8. Recursion and Dynamic Programming

## 8-1 ) Triple Step : A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
```python
# 피보나치 수열과 비슷
# n이 0일떄를 1로 보느냐 0으로 보느냐에 따라 코드가 달라질 듯
# n = 0일때 방법을 1으로 가정
def getPosWayCnt(n):
    way_cnts = [1, 1, 2]
    if n < 3:
        return way_cnts[n]
    for i in range(3, n+1):
        way_cnts.append(sum(way_cnts[i-3:i]))
    return way_cnts[n]
```
<hr>

## 8-2 ) Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
```python
# 참고 : 가짓수를 찾는 문제 https://velog.io/@tjdud0123/%EB%93%B1%EA%B5%A3%EA%B8%B8
# off limits(금지구역)가 2차 배열로 주어진다 가정 [x, y] ex) [[2, 2], [3, 2]]
# ? parameter가 많아져 global로 선언 => 오염문제 (어떻게 해야 가장 좋은가 ?)
def solution(r, c, limits):
    global r, c, limits
    limits = set([(y, x) for x, y in limits])
    cur_y, cur_x = 0, 0
    path = []
    return getPath(cur_y, cur_x, path)

def getPath(cur_y, cur_x, path):
    global r, c, limits
    
    path.append((cur_y, cur_x))
    if cur_y == r-1 and cur_x == c-1:
        return path

    # 아래 또는 오른쪽 이동
    DELTAS = {'D': (1, 0), 'R': (0, 1)}
    for dy, dx in DELTAS.values():
        nxt_y, nxt_x = cur_y + dy, cur_x + dx
        if visitable(nxt_y, nxt_x):
            getPath(nxt_y, nxt_x, path)
    #이동 불가
    if path:
        path.pop()
    else:
        return None

def visitable(nxt_y, nxt_x):
    global r, c, limits
    isOffLimit = (nxt_y, nxt_x) in limits
    return 0 <= nxt_y < r and 0 <= nxt_x < c and not isOffLimit

```
<hr>

## 8-3 ) Magic Index: A magic index in an array A[e... n-1] is defined to be an index such that A[ i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
```python
# 정렬되어있고 같은원소가 아니라는 것이 관건
# 포인터를 두고 arr를 복사하지 않는것이 효율적!

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

```

```python
# 같은 원소가 있을때는 brute force한 방법밖엔 모르겠음
def getMagicIdx(n, arr):
    for i in range(n):
        if arr[i] == i:
            return i
    return None

```
<hr>

## 8-4 ) Power Set: Write a method to return all subsets of a set.
```python
# 방법 1 DP => 이전 조합 + 자기자신 원소
# reduce 사용
def getPowerSet(arr):
    return reduce(lambda result, el: getSubSets(result, el), arr, [[]])
def getSubSets(result, el):
    new_subs = [subset + [el] for subset in result]
    return result + new_subs
```

```python
# 방법 2 라이브러리 사용
from itertools import combinations
def getPowerSet(arr):
    p_sets = []
    for i in range(len(arr)+1):
        p_sets += [sets for sets in combinations(arr, i)]
    return p_sets
```
<hr>

## 8-6 ) Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following constraints:
```python
def hanoi(num, fr, to, temp, moves):
    if num == 1:
        moves.append([fr,to])
    else:
        hanoi(num-1, fr, temp, to, moves)
        moves.append([fr,to])
        hanoi(num-1, temp, to, fr, moves)

def solution(n):
    moves = []
    hanoi(n, 1, 3, 2, moves)
    return moves
```
<hr>

## 8-7 )Permutations without Dups: Write a method to compute all permutations of a string of unique characters.
```python
def getPermuts(string):
    result = []
    for i, char in enumerate(string):
        rest = string[:i] + string[i+1:]
        subs = [char + sub for sub in getPermuts(rest)] if rest else [char]
        result += subs
    return result
```
<hr>

## 8-9 ) Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
```python
def getParens(n):
    parens = [set([]) if i else set(['()']) for i in range(n)]
    
    for i in range(1, n):
        for paren in parens[i-1]:
            for j in range(len(paren)+1):
                new_el = paren[:j] + '()' + paren[j:]
                parens[i].add(new_el)
    return parens[i] if n > 1 else None

```
<hr>


## 8-10 )Paint Fill: Implement the "paint nil" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, nil in the surrounding area until the color changes from the original color.
```python
# point = (x, y)
from collections import deque


def fillPaint(screen, point, new_color):
    r, c = len(screen), len(screen[0])
    y, x = point
    old_color = screen[y][x]

    if not visitable(y, x, r, c):
        return False

    DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    que, visited = deque([point]), set([point])
    while que:
        cur_y, cur_x = que.popleft()
        screen[cur_y][cur_x] = new_color
        visited.add((y, x))
        for dy, dx in DELTAS:
            nxt_y, nxt_x = cur_y + dy, cur_x + dx
            # 방문 불가
            if not visitable(nxt_y, nxt_x, r, c) or (nxt_y, nxt_x) in visited:
                continue
            # 방문 가능하지만 같은컬러만 색칠
            if screen[nxt_y][nxt_x] == old_color:
                que.append((nxt_y, nxt_x))

def visitable(nxt_y, nxt_x, r, c):
    return 0 <= nxt_y < r and 0 <= nxt_x < c

```
<hr>

## 8-11 ) Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.
```python
# 맞는지 모르겠음
def solution(amount):
    QUARTER, DIME, NICKEL, PENNY = 25, 10, 5, 1
    coin_units = [QUARTER, DIME, NICKEL, PENNY]
    # 큰 화폐부터 -> 거꾸로 sort
    coin_units = sorted(coin_units, reverse=True)
    return getCoinsWayCnt(coin_units, amount)

def getCoinsWayCnt(coin_units, amount):
    if (amount == 0):
        return 1;

    cnt = 0;
    for unit in coin_units:
        if amount - unit >= 0:
            cnt += nCents(amount - unit)
    return cnt;
}
```
<hr>

## 8-12 ) Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.
```python
# N-queen : 문제 n = 8일때
solution(8)
def dfs(n, y, col, diag1, diag2):
    global answer
    if y == n:
        answer += 1
        return

    for x in range(n):
        if x in col or (x + y) in diag1 or (x - y) in diag2:
            continue
        col.add(x)
        diag1.add(x + y)
        diag2.add(x - y)
        dfs(n, y+1, col, diag1, diag2)
        col.remove(x)
        diag1.remove(x + y)
        diag2.remove(x - y)


def solution(n):
    global answer
    col, diag1, diag2 = set(), set(), set()
    answer = 0
    dfs(n, 0, col, diag1, diag2)
    return answer
```
<hr>


<hr>
<hr>
