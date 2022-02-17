## 4-1 ) Route Between Nodes : Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

# input 과 output 예시가 있었으면 좋겠음
# ex) vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import defaultdict, deque

def checkHasRoute(vertex, start, end):
    # init
    nodes = defaultdict(list)
    for v1, v2 in vertex:
        nodes[v1].append(v2)
    que, visited = deque([start]), set([start])
    # 탐색 - BFS
    while que:
        cur_node = que.popleft()
        for nxt_node in nodes[cur_node]:
            if nxt_node in visited:
                continue
            if nxt_node == end:
                return True
            que.append(nxt_node)
            visited.add(nxt_node)
    return False