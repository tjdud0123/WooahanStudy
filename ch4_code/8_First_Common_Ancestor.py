## 4-8 ) First Common Ancestor : Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

# Avoid storing additional nodes in a data structure 조건을 못봤음
# set을 쓰지않고 부모따라가는 방법 이해 필요
from collections import deque

def findFirstComAnc(node1, node2):
    parent_set = set()
    nodes = deque([node1, node2])
    while nodes:
        node = nodes.popleft()
        if node.parent:
            if node.parent in parent_set:
                return node.parent
            else:
                parent_set.add(node.parent)
                nodes.append(node.parent)
        else: # 루트
            return node