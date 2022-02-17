## 4-6 ) Successor : Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.

# BST - 중위 순회
def Successor(node):
    if not node:
        return None
    # 오른쪽중 가장 왼쪽
    if node.right:
        cur_node = node.right
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node
    # 부모의 왼쪽이 나면 부모가 다음 노드
    else:
        cur_node, parent_node = node, node.parent
        while parent_node and parent_node.left != cur_node:
            cur_node, parent_node = parent_node, parent_node.parent
        return parent_node