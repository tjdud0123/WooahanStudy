## 4-5 ) Validate BST : Implement a function to check if a binary tree is a binary search tree.

# 왼쪽 모든 노드 <= 현재 노드 < 오른쪽 모든 노드
checkBST(node, float('-inf'), float('inf'))

def checkBST(node, min_val, max_val):

    if not node:
        return True

    if node.data <= min_val or node.data > max_val:
        return False

    check_left = checkBST(node.left, min_val, node.data)
    check_right = checkBST(node.right, node.data, max_val)

    return check_left and check_right
