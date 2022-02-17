# Chapter4. Stacks and Queues

## 4-1 ) Route Between Nodes : Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

```python
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

```
<hr>

## 4-2 ) Minimal Tree : Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def createBST(arr):
    if not arr:
        return None

    mid_idx = len(arr) // 2
    mid_node = Node(arr[mid_idx])
    
    mid_node.left = createBST(arr[:mid_idx])
    mid_node.right = createBST(arr[mid_idx+1:])

    return mid_node
```
<hr>

## 4-3 ) List of Depths : Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

```python
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


```
<hr>

## 4-4 ) Check Balanced : Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

```python
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
```
<hr>

## 4-5 ) Validate BST : Implement a function to check if a binary tree is a binary search tree.

```python
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
```
<hr>

## 4-6 ) Successor : Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.

```python
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
```
<hr>

## 4-8 ) First Common Ancestor : Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
```python
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
```
<hr>

## 4-12 ) Paths with Sum : You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

```python
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


```
<hr>

<hr>
<hr>

#### 수업 노트

# 4-9 BST Sequence 
> 콤비네이션 리컬시브하게
# 4-10 Check Subtree
> T2가 작으므로 T1에서 루트 노드를 찾고나서 포인터를 따라가며 비교
> 같은 데이터가 있는경우에도 동작
# 4-11 Random Node
> 다른 메소드도 짜야하는 걸 보면 출제자의 의도는 Random Node에 최적화된 새로운구조
> 배열은 공간낭비 => heap 생성
