## 4-3 ) List of Depths : Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

from collections import deque

def createSameDepthLists(root):
    level_table = { 0: [root] }
    que = deque([(root, 0)])
    # 탐색 - level_table 저장
    while que:
        cur_root, cur_level = que.popleft()
        level_table.get(cur_level, []) + [cur_root]
        if cur_root.left:
            que.append((root.left, cur_level+1))
        if cur_root.right:
            que.append((root.right, cur_level+1))
    # linkedList 생성
    result = []
    for level, nodes in level_table:
        linked_list = new LinkedList()
        for node in nodes:
            linked_list.append(node)
        result.append(linked_list)

    return result
