## 4-12 ) Paths with Sum : You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# dfs를 쓰면 될것같은데 잘 안되어서 찾아봄
# global로 선언
def getCntSumIsTarget(root, target):
    global cnt, path
    cnt, path = 0, []
    checkSumIsTarget(root, target)
    return cnt

def checkSumIsTarget(root, target):
    global cnt, path

    if not root:
        return

    path.append(root.data)
    checkSumIsTarget(root.left, target)
    checkSumIsTarget(root.right, target)

    cost = 0
    # 위에서 부터 내려올 수 있으므로 거꾸로 연산
    for num in path[::-1]:
        cost += num
        if cost == target:
            cnt += 1

    path.pop()
