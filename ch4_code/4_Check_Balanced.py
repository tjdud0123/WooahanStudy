## 4-4 ) Check Balanced : Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

# 시간복잡도가 높음 => nlogn => 더 좋은 풀이 이해필요!
# 자식이 없는 노드 높이를 0으로 보기도함 
def checkBalanced(root):
    BALANCED_H = 1
    if not root:
        return True

    height_diff = abs(getH(root.left) - getH(root.right))
    if height_diff > BALANCED_H:
        return False
    else:
        return checkBalanced(root.left) and checkBalanced(root.right)

def getH(root):
    return max(getH(root.left), getH(root.right)) + 1 if root else 0
