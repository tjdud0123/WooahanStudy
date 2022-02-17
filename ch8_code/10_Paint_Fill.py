## 8-10 )Paint Fill: Implement the "paint nil" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, nil in the surrounding area until the color changes from the original color.

# point = (x, y)
from collections import deque


def paintFill(screen, point, new_color):
    r, c = len(screen), len(screen[0])
    y, x = point
    old_color = screen[y][x]

    if not (0 <= y < r and 0 <= x < c):
        return False

    DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    que, visited = deque([point]), set([point])
    while que:
        cur_y, cur_x = que.popleft()
        screen[cur_y][cur_x] = new_color
        for dy, dx in DELTAS:
            nxt_y, nxt_x = cur_y + dy, cur_x + dx
            # 방문 불가
            if not visitable(nxt_y, nxt_x, r, c) or (nxt_y, nxt_x) in visited:
                continue
            # 방문 가능하지만 같은컬러만 색칠
            if screen[nxt_y][nxt_x] == old_color:
                que.append((nxt_y, nxt_x))

def visitable(nxt_y, nxt_x, r, c):
    return 0 <= nxt_y < r and 0 <= nxt_x < c and not isOffLimit    
