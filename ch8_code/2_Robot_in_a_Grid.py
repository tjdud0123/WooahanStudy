## 8-2 ) Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

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