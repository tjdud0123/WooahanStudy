# 8-12 ) Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.

# 참고 : 예전에 N-queen 문제를 푼 적있음 https://velog.io/@tjdud0123/N-Queen

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