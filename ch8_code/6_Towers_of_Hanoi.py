## 8-6 ) Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following constraints:

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